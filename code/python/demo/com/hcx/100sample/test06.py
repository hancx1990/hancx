#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：斐波那契数列。第三个数等于前两个数字之和
"""


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fib(10))


def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(10))


def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


res = fib3(10)
print(res[res.__len__() - 1])

