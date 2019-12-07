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
