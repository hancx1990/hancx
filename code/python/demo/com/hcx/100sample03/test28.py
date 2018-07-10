#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：有5个人坐在一起，问第五个人多少岁，他说比第四个大两岁，问第四个，他说比第三个大两岁，依次类推，问第一个，他说十岁？
"""


def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1) + 2


print(age(5))