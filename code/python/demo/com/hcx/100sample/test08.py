#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输出9*9乘法口诀
"""

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print('%d * %d = % - 3d' % (i, j, result))


print("-------------------")
for i in range(1, 10):
    for j in range(i, 10):
        result = i * j
        print('%d * %d = % - 2d' % (i, j, result))