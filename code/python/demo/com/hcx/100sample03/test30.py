#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：一个五位数，判断他是不是回数，即12321是回文数，个位与万位相同，十位与千位相同。
"""
x = input('input a number:')
x = str(x)
flag = False
for i in range(int(len(x) / 2)):
    if x[i] != x[-i - 1]:
        flag = False
        break
    flag = True
print("--------------")

if flag:
    print('这是一个回文数')