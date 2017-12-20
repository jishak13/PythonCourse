# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:00:38 2017

@author: JoeRemote
"""

"Lambda Expressions!!!"


def square(num):
    result = num**2
    return result


square(2)

def square(num):
    return num**2
square(3)


square = lambda num: num**2


square(10)


"Check if a number is even

even = lambda num: num%2==0
even(3)


first = lambda s: s[0]

first('hello')



adder = lambda x,y: x+y

adder(2,10)