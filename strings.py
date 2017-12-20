# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 09:00:20 2017

@author: JoeRemote
"""
from __future__ import print_function
"Creating Strings"

print 'Hello'

"Printing Strings"
print "This is a string\nHere is a new line"
print "This is a string\tHere is a tab "


"Differences in 3 and 2"
print('hello world')

"Length of the sequence"
len("Hello World")


"Indexing"
s = 'Hello World'

print (s)

print(s[3])

"3: mean onward, give me evertynig from the third index and  onward
print(s[3:])

":3 mean up to, give me evertynig up third index
print(s[:3])

"grab everything"
print(s[:])

print(s[-1])

print(s[:-1])

print(s[::1])

print(s[::2])

"reversing a string"
print(s[::-1])


"immutability - once the string is created the elements cannot be changed"

print s + " Concatenate me!"


letter = 'z'

print letter*10

s = "hello"


s.upper()

s.lower()

s.split('e')

