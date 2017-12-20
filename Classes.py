# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:24:30 2017

@author: JoeRemote
"""

"Objects"

class Sample(object):
    pass

x = Sample()
type(x)


class Dog(object):
    
    
    #Class object attribute
    #no matter what object we make, the species will be a mammal
    #These are like static variables
    species = 'mammal'
    
    #should always be the first method
    #always start with self in the parameters
    def __init__(self, breed,name):
        self.breed= breed
        self.name = name
    
   
sam = Dog(breed='lab',name = 'sam')
sam.breed
sam.species
sam.name


class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi
    
    def set_radius(self,new_radius):
        self.radius = new_radius
    
    def get_radius(self):
        return self.radius
    

        
    
c = Circle(radius =100)
c.pi
c.radius
c.area()
c.set_radius(50)
c.area()
c.get_radius()