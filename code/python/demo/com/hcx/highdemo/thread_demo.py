#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _thread
import time


def print_time(threadName, delay):
    "定义一个函数"
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("Thread-1", 2))
    _thread.start_new_thread(print_time, ("Thread-2", 3))
except:
    print("Error: unable to start thread")

while 1:
    pass