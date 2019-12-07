# coding=utf-8
"""
EXCEL 操作函数
"""


def gen_excel_row_line(excel_path, sheet_index=0):
    """
    生成excel以行为返回单位的迭代器
    :param sheet_index: sheet的索引
    :param excel_path: excel的路径
    :return:
    """
    import xlrd
    book = xlrd.open_workbook(excel_path)
    if type(sheet_index) is int:
        sheet = book.sheet_by_index(sheet_index)
    else:
        sheet = book.sheet_by_name(sheet_index)
    rows = sheet.nrows
    for i in xrange(rows):
        row = sheet.row_values(i)
        yield i, row


def gen_excel_col_line(excel_path, sheet_index=0):
    """
    生成excel以列为返回单位的迭代器
    :param sheet_index: sheet的索引
    :param excel_path: excel的路径
    :return:
    """
    import xlrd
    book = xlrd.open_workbook(excel_path)
    if type(sheet_index) is int:
        sheet = book.sheet_by_index(sheet_index)
    else:
        sheet = book.sheet_by_name(sheet_index)
    cols = sheet.ncols
    for j in xrange(cols):
        col = sheet.col_values(j)
        yield j, col


def write_excel_row_lines(excel_path, sheet_names, lines):
    """
    将lines写入Excel的sheet_name名列表
    :param excel_path: 路径
    :param sheet_names: 写入sheet名字列表
    :param lines: 行数据
    :return:
    """
    import xlwt
    write_book = xlwt.Workbook(encoding="utf-8")
    for i, one_name in enumerate(sheet_names):
        sheet = write_book.add_sheet(one_name)
        sheet_line = lines[i]
        for row, one_line in enumerate(sheet_line):
            for col, one_col in enumerate(one_line):
                sheet.write(row, col, one_col)
    write_book.save(excel_path)
