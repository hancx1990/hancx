#!/usr/bin/python
# -*- encoding: UTF-8 -*-
flag = False
name = 'test'
if name == 'test':
    flag = True
    print('welcome boss')
else:
    print(name)

num = 5
if num == 3:
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:
    print('error')
else:
    print('roadman')

num = 9
if num >= 0 and num <= 10:
    print('hello')

if num < 0 or num > 10:
    print('hello')
else:
    print('undefine')
