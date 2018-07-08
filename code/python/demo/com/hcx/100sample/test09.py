#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：暂停一秒输出
"""

import time

myD = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g'}
for key,value in dict.items(myD):
    print(key, value)
    time.sleep(1)
