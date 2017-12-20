# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:43:26 2017

@author: JoeRemote
"""

class Animal(object):
    
    def __init__(self):
      print("Animal Created")
      
     
    def whoAmI(self):
        print("Animal")
        
    def eat(self):
        print("Eating")
        
class Dog(Animal):
    
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
    def whoAmI(self):
        print("Dog")
    
    def bark(self):
        print("Woof")


d = Dog()

d.bark()
d.eat()