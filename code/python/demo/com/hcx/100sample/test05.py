#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输入三个整数x,y,z请把这三个数有小到大输出。
"""

m = []
for i in range(0, 3):
    n = int(input('input:\n'))
    m.append(n)
m.sort()
print(m)
m.sort(reverse=True)
print(m)
m.sort(reverse=False)
print(m)