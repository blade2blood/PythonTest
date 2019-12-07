# coding=utf-8
"""
国家数据处理
"""

import pprint
import common_util


common_util.path_op.add_module_search_path("../lib")


def gen_all_country_excel(path_name):
    path_op = common_util.path_op
    for excel_name in path_op.gen_all_file_name(path_name, need_type="xlsx"):
        yield excel_name


def main(path_name):
    log = common_util.log_op.file_log("./log.txt")
    excel_op = common_util.excel_op
    for excel in gen_all_country_excel(path_name):
        log("start process excel is:%s", excel)
        log("start sheet 0 Export FOB:")
        for row, line in excel_op.gen_excel_row_line(excel, 0):
            pprint.pprint(line)
        log("start sheet 1 Import CIF:")
        for row, line in excel_op.gen_excel_row_line(excel, 1):
            pprint.pprint(line)
        log("process excel: %s finish!", excel)
    log.log_finish()


if __name__ == "__main__":
    main("./data")
