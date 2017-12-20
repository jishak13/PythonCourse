# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:48:39 2017

@author: JoeRemote
"""

def printName():
    print "hi Joe"
    
    
    
printName()


def printVariables(x,y):
    print 'Number 1: %s Number 2: %s',x,y
    
printVariables(1,2)


def addVariables(x,y):
    return x+y

x = addVariables(2,4)
x

def is_prime(num):
    """
    Checks for a prime number
    """
    for n in range(2,num):
        if num % n == 0:
            print "Not Prime"
            break
    else: 
        print 'The number is prime'
        
is_prime(12)