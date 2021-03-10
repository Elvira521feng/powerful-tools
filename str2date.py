# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 10:18 上午
# @Author  : JiangYanQun
# @File    : str2date.py
import re
import datetime

from dateutil.parser import parse
from constant import CN_NUM


def str2date(start_time_str):
    """
    将到到期日中的大写中文字符转化为标准数字格式
    2020年1月1日 --> 2020-1-1
    """
    list_s = [i for i in start_time_str]
    num_list = []

    for index, s in enumerate(list_s):
        list_s[index] = CN_NUM.get(s, s)
        if isinstance(list_s[index], int):
            num_list.append((index, str(list_s[index])))

    # 判断类型，利用是否为数字，将几组数字找出来然后组合
    str_num = ''
    flag = 0
    if num_list:
        str_num = num_list[0][1]
        str_flag = num_list[0][0]
        for num in num_list[1:]:
            if num[0] - str_flag == 1:
                str_flag = num[0]
                str_num += num[1]
            else:
                str_flag = num[0]
                str_num = str_num + '-' + num[1]
                flag += 1

    if flag == 0 and len(str_num) > 4:
        try:
            str_n = str(parse(str_num))
            str_num = str_n.split(' ')[0]
        except Exception as e:
            print(e)
            str_num = ''

    if len(str_num):  # 不为空的情况下转换时间格式
        if validate_date(str_num):
            str_num, flag = match_date(str_num)
        else:
            str_num = None  # 默认时间

    return str_num


def validate_date(text):
    """
    验证日期格式
    :param text: 待检索文本
    >>> validate_date('2020-05-20')
    True
    >>> validate_date('2020-05-32')
    False
    """
    try:
        if datetime.datetime.strptime(text, '%Y-%m-%d').strftime('%Y-%m-%d'):
            return True
    except ValueError:
        try:
            if datetime.datetime.strptime(text, '%Y-%m').strftime('%Y-%m'):
                return True
        except ValueError:
            try:
                if datetime.datetime.strptime(text, '%m-%d').strftime('%m-%d'):
                    return True
            except ValueError:
                try:
                    if datetime.datetime.strptime(text, '%m').strftime('%m'):
                        return True
                    else:
                        raise ValueError
                except ValueError:
                    return False


def validate_datetime(text):
    """
    验证日期+时间格式
    :param text: 待检索文本
    >>> validate_datetime('2020-05-20 00：00：00')
    True
    >>> validate_datetime('2020-05-32 00：00：00')
    False
    """
    try:
        if text == datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'):
            return True
        else:
            raise ValueError
    except ValueError:
        return False


def match_date(text):
    """
    正则表达式提取文本所有日期
    :param text: 待检索文本
    >>> match_date('日期是2020-05-20')
    ['2020-05-20']
    """
    pattern_ymd = r'(\d{4}-\d{1,2}-\d{1,2})'
    pattern_ym = r'(\d{4}-\d{1,2})'
    pattern_md = r'(\d{1,2}-\d{1,2})'
    pattern_m = r'(\d{1,2})'
    flag = True

    pattern = re.compile(pattern_ymd)
    result = pattern.findall(text)
    if not result:
        pattern = re.compile(pattern_ym)
        result = pattern.findall(text)
        flag = False

    if not result:
        pattern = re.compile(pattern_md)
        result = pattern.findall(text)
        flag = False

    if not result:
        pattern = re.compile(pattern_m)
        result = pattern.findall(text)
        flag = False

    return result[0], flag


def match_datetime(text):
    """
    正则表达式提取文本所有日期+时间
    :param text: 待检索文本
    >>> match_datetime('日期是2020-05-20 13:14:15.477062.')
    ['2020-05-20 13:14:15']
    """
    pattern = r'(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})'
    pattern = re.compile(pattern)
    result = pattern.findall(text)
    return result