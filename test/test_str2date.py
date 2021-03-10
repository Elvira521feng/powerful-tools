# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 5:24 下午
# @Author  : JiangYanQun
# @File    : test_str2date.py
from str2date import str2date


def test():
    test_dig = ['2020年1月1日',
                # '200年1月1日',
                # '2020年月1日',
                '1月2日',
                '2020年2月',
                # '2020年1月132日',
                '2020年123月日']
    for cn in test_dig:
        x = str2date(cn)
        if x:
            print("格式转换成功：", cn, '-->', x)
        else:
            print('格式转换失败：'+'"' + cn + '"时间格式不对！')


if __name__ == '__main__':
    test()
