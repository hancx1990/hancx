#!/usr/bin/python
# -*- coding: UTF-8 -*-
count = 0
while(count < 9):
    print('the count is:',count)
    count = count + 1
print("good bye!")

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

var = 1
while var == 1:
    num = input("Enter a number :")
    print("You entered:",num)
    break
print("good bye!")