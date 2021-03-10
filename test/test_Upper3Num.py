# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 5:34 下午
# @Author  : JiangYanQun
# @File    : test_Upper3Num.py
from Upper2Num import amount_convert


def test():
    test_dig = ['198万',
                '19.8万',
                '0.98万',
                '198',
                '180000',
                '十一',
                '一百二十三',
                '一千二百零三',
                '一万一千一百零一',
                '十万零三千六百零九',
                '一百二十三万四千五百六十七',
                '一千一百二十三万四千五百六十七',
                '一亿一千一百二十三万四千五百六十七',
                '一百零二亿五千零一万零一千零三十八']
    for cn in test_dig:
        x = amount_convert(cn)
        print(cn, x)


if __name__ == '__main__':
    test()
