#!/use/bin/python
# -*- coding: UTF-8 -*-
counter = 100
miles = 1000.0
name = "Jhon"
print(counter)
print(miles)
print(name)

a = b = c = 1
print(a,b,c)
a, b, c = 1, 2, "john"

print(a)
print(b)
print(c)

str = 'Hello World!'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())