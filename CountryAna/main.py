# coding=utf-8
"""
国家数据处理
"""

import common_util


common_util.path_op.add_module_search_path("../lib")


def gen_all_country_excel(path_name):
    path_op = common_util.path_op
    for excel_name in path_op.gen_all_file_name(path_name, need_type="xlsx"):
        yield excel_name


def preprocess_cell(line):
    line = filter(bool, line)

    def to_str(x):
        if type(x) is unicode:
            return x.encode("utf-8")
        else:
            return str(x)
    line = map(to_str, line)
    return line


country_data = [{}, {}]  # 出口 进口
write_one_sheet = True


def add_country_export_data(country1, country2, data):
    country_data[0].setdefault(country1, {})[country2] = data


def add_country_import_data(country1, country2, data):
    country_data[1].setdefault(country1, {})[country2] = data


def process_data(excel_op, excel, log, index, add_func, log_str):
    left = None
    for row, line in excel_op.gen_excel_row_line(excel, index):
        line = preprocess_cell(line)
        if row == 3:
            left = line[0]
            log(log_str + " Find Left Country:%s", left)
        if left:
            if len(line) >= 2:
                add_func(left, line[0], line[1])


def write_country_data():
    """
    写入分开的sheet
    :return:
    """
    lines = []
    for i in xrange(2):
        tmp_sheet_line = []
        for country1, dd in country_data[i].iteritems():
            for country2, v in dd.iteritems():
                tmp_sheet_line.append([country1, country2, v])
        tmp_sheet_line.sort()
        lines.append(tmp_sheet_line)

    common_util.excel_op.write_excel_row_lines(
        "./data/combine_all_country.xls",
        ["Export", "Import"], lines
    )


def write_country_data_one_sheet():
    """
    写入一个sheet
    :return:
    """
    lines = [["country1", "country2", "Export", "Import"]]
    tmp_dict = {}
    for i, data in enumerate(country_data):
        for country1, dd in data.iteritems():
            for country2, v in dd.iteritems():
                tmp_dict.setdefault((country1, country2), ["empty", "empty"])[i] = v
    tmp_lines = []
    for k, v in tmp_dict.iteritems():
        one_line = list(k)
        one_line.extend(v)
        tmp_lines.append(one_line)
    tmp_lines.sort()

    lines.extend(tmp_lines)
    common_util.excel_op.write_excel_row_lines(
        "./data/combine_all_country_one_sheet.xls",
        ["ExportAndImport"], [lines]
    )


def main(path_name):
    log = common_util.log_op.file_log("./log.txt")
    std_log = common_util.log_op.std_log
    excel_op = common_util.excel_op
    std_log("正在读取Excel.....")
    for excel in gen_all_country_excel(path_name):
        log("start process excel is:%s", excel)

        log("start sheet 0 Export FOB:")
        process_data(excel_op, excel, log, 0, add_country_export_data, "Export")

        log("start sheet 1 Import CIF:")
        process_data(excel_op, excel, log, 1, add_country_import_data, "Import")

    std_log("正在写入Excel.....")
    if write_one_sheet:
        write_country_data_one_sheet()
    else:
        write_country_data()
    log.log_finish()
    std_log("处理完毕...")


if __name__ == "__main__":
    main("./data")
