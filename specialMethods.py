# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:48:42 2017

@author: JoeRemote
"""

l = [1,2,3]

print(l)



class Book(object):
    
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        print("A book has been created")
        
        #Like an override of to string
    def __str__(self):
        return "Title: %s, Author: %s, pages %s " %(self.title,self.author,self.pages)


    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("The book is gone!")

b = Book('Python','Jose',100)

len(b)

del b