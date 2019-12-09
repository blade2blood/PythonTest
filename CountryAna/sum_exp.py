# -*- coding:utf-8 -*-
"""
    Author: wenjiangye@corp.netease.com
    File: sum_exp.py
    Date: 2019/12/9 23:23
    Desc: 将fit_exp
"""
import common_util


def gen_fit_trade_data(excel="./data2/fitvalue.csv"):
    res = {}
    for row, line in common_util.excel_op.gen_csv_row_line(excel):
        if row != 0:
            _, code1, code2, fit_value, fit_exp = line
            code1 = eval(code1)
            res.setdefault(code1, 0)
            res[code1] += eval(fit_exp)
    res = res.items()
    res.sort()
    return res


def main():
    res = gen_fit_trade_data()
    res.insert(0, ("Code1", "AllExp"))
    common_util.excel_op.write_excel_row_lines("./data2/sum_fit_exp.xls", ["SumExp"], [res])


if __name__ == "__main__":
    main()

