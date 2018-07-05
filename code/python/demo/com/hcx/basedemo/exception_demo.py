#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("aaaa.txt", "w")
    fh.write()
except TypeError:
    print("Error:没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()