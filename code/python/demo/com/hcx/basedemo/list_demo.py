#!/usr/bin/python
# -*- coding: UTF-8 -*-
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(list1[0])
print(list2[1:5])

list = []
list.append('google')
list.append('runoob')
print(list)

print('before del value', list1)
del list1[2]
print('after del value', list1)
