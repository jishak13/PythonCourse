# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:37:10 2017

@author: JoeRemote
"""

l = []

for letter in 'word':
    l.append(letter)
    
print l


l = [letter for letter in 'word']


lst = [x**2 for x in range(0,11)]

print lst

lst = [number for number in range(11) if number % 2 == 0]


celsius = [0,10,20.1,34.5]
fahrenheit = [ (temp*(9/5.0) + 32 ) for temp in celsius]

fahrenheit


lst = [ x**2 for x in [ x**2 for x in range(11)] ]

lst