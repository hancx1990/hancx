#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：一个数如果恰好等于它的因子之和，这个数就称为“壳数”。例如6=1=2=3
"""
from sys import stdout

for j in range(2, 1001):
    k = []
    n = -1
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i
            k.append(i)
    if s == 0:
        print(j)
        for i in range(n):
            print(k[i],end='')
        print(k[n])