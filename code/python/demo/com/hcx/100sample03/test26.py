#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：利用递归方法求5！
"""


def sum_fact(n):
    """
    阶乘
    :param n:参数
    :return:返回值
    """
    if n == 1:
        return 1
    else:
        return sum_fact(n - 1) * n


print(sum_fact(5))
