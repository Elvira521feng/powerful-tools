# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 3:26 下午
# @Author  : JiangYanQun
# @File    : Upper2Num.py


import re

from constant import CN_UNIT, CN_NUM


def chinese_to_arabic(cn: str) -> int:
    """
    中文大写数字转换成阿拉伯数字
    :param cn: 中文大写数字
    :return: 阿拉伯数字
    """
    unit = 0  # 单位
    ldig = []  # digest
    for cndig in reversed(cn):
        if cndig in CN_UNIT:
            unit = CN_UNIT.get(cndig)
            if unit == 10000 or unit == 100000000:
                ldig.append(unit)
                unit = 1
        else:
            dig = CN_NUM.get(cndig)
            if unit:
                dig *= unit
                unit = 0
            ldig.append(dig)
    if unit == 10:
        ldig.append(10)
    val, tmp = 0, 0
    for x in reversed(ldig):
        if x == 10000 or x == 100000000:
            val += tmp * x
            tmp = 0
        else:
            tmp += x
    val += tmp
    return val


def amount_convert(amount_text, standard_unit=''):
    """
    对金额进行标准化转换
    三种类型：全是大写、整数+单位、小数+单位
    """
    amount_num = None
    num_pattern = re.compile(r'\d')
    has_num = True if num_pattern.search(amount_text) else False
    float_unit_pattern = re.compile(r'(?P<number>[\d.]+)(?P<unit>[万萬亿億]?)')
    if has_num:
        res_float = float_unit_pattern.search(amount_text)
        if res_float:
            number = res_float.group('number')
            unit = res_float.group('unit')
            amount_num = float(number) * CN_UNIT[unit]
    else:
        amount_num = chinese_to_arabic(amount_text)

    amount_num = amount_num / CN_UNIT[standard_unit]

    return format(round(amount_num, 5), '.4f')  # 保留4为小数
