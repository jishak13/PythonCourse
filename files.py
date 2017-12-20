# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 09:56:57 2017

@author: JoeRemote
"""

f = open('myFile.txt')

f.read()

f.seek(0)

f.read()

f.seek(0)

"Stores the lines in memory"
f.readlines()

%%writefile new.txt
First Line
Second Line

for line in open('new.txt'):
    print(line)