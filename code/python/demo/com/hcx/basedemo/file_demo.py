#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


fi = open("E:/MS/hancx/code/python/demo/com/hcx/basedemo/file_demo.py", "r")
print(fi.name)
print(fi.read())
os.rename("hello1.py", "hello.py")
fi.close()