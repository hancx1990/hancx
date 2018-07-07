#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

print(re.match('www', 'www.baidu.com').span())
print(re.match('com', 'www.baidu.com'))

line = "Cats are smarter than dogs"

mathchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if mathchObj:
    print(mathchObj.group())
    print(mathchObj.group(1))
    print(mathchObj.group(2))
else:
    print("No match!!")

print(re.search('www', 'www.baidu.com').span())
print(re.search('com', 'www.baidu.com').span())

print('demo---------------------')
phone = "2004-595-559 # 这是一个国外电话号码"

num = re.sub(r'#.*$', "", phone)
print(num)

num = re.sub(r'\D', "", phone)
print(num)

print("--------------------")


def double(matched):
    "将匹配的数字乘以2"
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))