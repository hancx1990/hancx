#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：有一对兔子，从出生后第三个月都生一对兔子，小兔子长到三个月后每个月生一对兔子，假如兔子都不死，问每个月的兔子总数？
1,1,2,3,5,8,13
"""

f0 = 1
f1 = 1
f2 = 2
for i in range(1, 21):
    print('%12d %12d' % (f1, f2))
    f1 = f1 + f2
    f2 = f1 + f2


def rest(n):
    if n == 1 or n == 2:
        return 1
    return rest(n - 1) + rest(n - 2)


for i in range(1, 41):
    print('%12d %12d ' % (i, rest(i)))