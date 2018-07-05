#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar

ticks = time.time()
print(ticks)
print(time.localtime(ticks))
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
a = "Thu Jul 05 22:09:20 2018"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

cal = calendar.month(2018, 7)
print(cal)
