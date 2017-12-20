# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:59:30 2017

@author: JoeRemote
"""
"Try Except is like try Catch"
try:
   2 + 's'
except TypeError:
    print("There was a type Error")
    
"else and finally statements within the Try"
try: 
    f = open('testfile','r')
    f.write('Test write this ')
except:
    print('Error in writing to the file!')
else: 
    print('File write was a succcess')
finally:
    print('This always runs')
    
    
def askint():

    while True:
        
        try:
            val = int(input('Please enter an integer: '))
        except:
            print('Looks like you did not enter and integer!')
            continue
        else:
            print('Correct, that is an integer!')
            break
        finally:
            print('Finally Executed')
            
        print(val)
    
askint()
    
            
        