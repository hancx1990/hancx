#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：将一个正整数分解质因数。如：90 = 2*3*3*5
"""
import sys


n = int(input("input number:"))
mm = n
print("n = %d" % n)
for i in range(2, n + 1):
    while n != i:
        if n % i == 0:
            print(i, end='')
            print("*", end='')

            n = n / i
        else:
            break

print("%d" % n, end='')
print(' =', mm)