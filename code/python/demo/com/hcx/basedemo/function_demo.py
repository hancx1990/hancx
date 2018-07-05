#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

def change_int(a):
    a = 10
    print(a)


b = 2
change_int(b)
print(b)


def change_me(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print(mylist)
    return


myList = [10, 20, 30]
change_me(myList)


def print_info(arg1, *vartuple):
    "打印任何传入的参数"
    print(arg1)
    for var in vartuple:
        print(var)
    return


print_info(10)
print_info(70, 60, 50)


total = 0


def sum1(arg1, arg2):
    "返回2个参数的和"
    total = arg1 + arg2
    print(total)
    return total


sum1(10, 20)
print(total)
print(sum1(10, 25))


content = dir(math)
print(content)