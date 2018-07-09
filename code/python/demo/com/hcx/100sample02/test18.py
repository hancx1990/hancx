#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：求s=a+aa+aaa+aaaa+.....a的值，其中a是一个数字。
"""
from functools import reduce

Tn = 0
Sn = []
n = int(input('n = :'))
a = int(input('a = :'))
for i in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)
Sn = reduce(lambda x, y: x + y, Sn)
print(Sn)