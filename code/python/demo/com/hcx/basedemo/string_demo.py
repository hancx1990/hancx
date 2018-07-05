#!/usr/bin/python
# -*- coding: UTF-8 -*-
var1 = 'hello world!'
var2 = 'python runoob'

print(var1[0])
print(var2[1:5])

a = 'hello'
b = 'python'
print(a + b)
print(a * 2)
print(a[1])
print(a[1:4])
if 'h' in a:
    print('h 在变量a中')
else:
    print('h 不在变量a中')

if 'm' not in a:
    print('m 不在变量a中')
else:
    print('m 在变量a中')
print(r'\n')
print(R'\n')

print("My name is %s and weight is %d kg!" % ('zara', 21))

print(a.capitalize())
print(a.center(10))