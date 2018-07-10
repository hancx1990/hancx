#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：给一个不多于5位数的正整数，要求：一、求它是几位，二，逆序打印出各位数字
"""
s = int(input('input a int:'))
a = int(s / 10000)
b = int(s % 10000 / 1000)
c = int(s % 1000 / 100)
d = int(s % 100 / 10)
e = int(s % 10)
if a != 0:
    print("there are 5 ", e, d, c, b, a)
elif b != 0:
    print("there are 4 ", e, d, c, b)
elif c != 0:
    print("there are 3 ", e, d, c)
elif b != 0:
    print("there are 2 ", e, d)
else:
    print("there are 1 ", e)