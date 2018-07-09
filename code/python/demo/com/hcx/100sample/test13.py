#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：打印出所有的水印花数，各位数字立方等于该数本身，如：153
"""

for n in range(100, 1000):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = int(n % 10)
    temp = i ** 3 + j ** 3 + k ** 3
#    print(i, j, k, temp)
    if n == temp:
        print(n)