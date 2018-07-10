#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印。
"""


def output(s, k):
    if k == 0:
        return
    print(s[k - 1], end='')
    output(s, k - 1)


s = input('input a string:')
l = len(s)
output(s, l)