# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:09:02 2017

@author: JoeRemote
"""

"For loops"

l = [1,2,3,4,5]
sum = 0
for element in l:
    sum += element
    
print sum


for nums in l:
    if nums % 2 == 0:
        print "I am even"
        
        
s = 'this is a string!'

for letter in s:
    print letter
    
    
"Iterating Tuples"
tup = (1,2,3,4,5)

for num in tup:
    print num
    
"Tuple Unpacking"
l = [(2,4),(6,8),(10,12)]

for (t1,t2) in l:
    print(t1)

"Dictionry"

d = {'k1': 1, 'k2': 2,'k3':3}

for item in d: 
    print item
    
for k,v in d.items():
    print k
    print v