# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:21:19 2017

@author: JoeRemote
"""

"While Statements"



x = 0

while x < 10:
    #do some code
    print 'x is currently: ',x
    x+= 1
    
x = 0
while x <10:
    print 'x is currently: ',x
    x +=1 

else: print 'All Done'


"break: Creaks out of the current closest enclosing loop"
"continue goes to the top of the closeset enclosing loop"
"pass nothing at all"

x = 0

while x < 10:
    print 'x is currently: ' ,x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    
    if x==3:
        print ' Hey x equals 3!'
        break
    else:
        print 'Continuing . . '
    continue
