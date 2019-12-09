# -*- coding:utf-8 -*-
"""
    Author: wenjiangye@corp.netease.com
    File: merge_excel.py
    Date: 2019/12/9 19:01
    Desc: 合并excel
"""
import common_util


def gen_70_trade_data(excel="./data2/70trade.xlsx"):
    res = {}
    for row, line in common_util.excel_op.gen_excel_row_line(excel):
        if row != 0:
            code1, code2, c1, c2, dist, t_gdp = line
            res[(code1, code2)] = [c1, code1, c2, code2, dist, t_gdp]
    return res


def gen_other_data(excel="./data2/161_all.xlsx"):
    res = {}
    for row, line in common_util.excel_op.gen_excel_row_line(excel):
        if row != 0:
            _, code1, code2, c1, c2, dist, n2, l2, n1, l1, bij, a2, a1 = line
            res[(code1, code2)] = [n2, l2, n1, l1, bij, a2, a1]
    return res


def main():
    log = common_util.log_op.file_log("./log_merge.txt")
    lines = []
    first_line = ["country1", "code1", "country2", "code2", "Dis", "t_gdp"]
    first_line.extend(["N2", "L2", "N1", "L1", "Bij", "A2", "A1"])
    lines.append(first_line)
    log("开始处理 70trade.xlsx")
    trade_data = gen_70_trade_data()
    log("开始处理 161_all.xlsx")
    other_data = gen_other_data()
    log("开始合并数据...")
    for (code1, code2), data in trade_data.iteritems():
        if (code1, code2) in other_data:
            data.extend(other_data[(code1, code2)])
            lines.append(data)
    log("合并完成, 开始写入...")
    common_util.excel_op.write_excel_row_lines("./data2/combine_all_data.xls", ["AllData"], [lines])
    log("写入完成...")
    log.log_finish_with_time()


if __name__ == "__main__":
    main()
