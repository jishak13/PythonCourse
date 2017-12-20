# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 09:30:15 2017

@author: JoeRemote
"""

my_list = [1,2,3]

print my_list[0]

my_list = [1,"string","true"]

len(my_list)


my_list = ["one","two","three",4,5]

my_list[1:]

my_list[:3]

my_list+["new","list"]


my_list*2


l = [1,2,3]


l.append(4)

l


print(l.pop())

x = l.pop(2)

x


l

new_list = ['a','e','x','b','c']

new_list.reverse()

new_list.sort()

new_list

l_1  = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1,l_2,l_3]

matrix[0]

matrix[0][2]

matrix[1][1]


"list comprehension"

first_col = [row[0] for row in matrix]

first_col 