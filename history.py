# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sat Dec 16 08:40:40 2017)---
runfile('C:/Users/JoeRemote/.spyder/temp.py', wdir='C:/Users/JoeRemote/.spyder')
runfile('C:/Users/JoeRemote/.spyder/numbers.py', wdir='C:/Users/JoeRemote/.spyder')
print 2**3
print 2 + 10 * 10 + 3
(2+10) * (10+3)
a=5
print a
print a+a
print a += a
print a + = a
a += a
print a
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print my_taxes
runfile('C:/Users/JoeRemote/.spyder/strings.py', wdir='C:/Users/JoeRemote/.spyder')
print "This is a string"
print "This is a string\n Here is a new line"
print "This is a string\tHere is a new line"
runfile('C:/Users/JoeRemote/.spyder/strings.py', wdir='C:/Users/JoeRemote/.spyder')
print('hello world')
len("Hello World")
s = 'Hello World'
print (s)
print(s[3])
print(s[3:])
print(s[:3])
print(s[:])
print(s[-1])
print(s[:-1])
print(s[::1])
print(s[::2])
print(s[::-1])
print s + "Concatenate me!"
letter = 'z'

print letter*10
s = "hello"
s.upper
s.upper()
s.encode()
s.lower()
s.split(1)
s.split()
s.split('e')
print "This is a string"
s = "String"
print "Place my variable here: %s" %(s)
print 'Floating point number: %1.2f' %(13.1245)
print 'Convert to String %s' %(123)
print 'Convert to STring %r' %(123)
print 'First : %s, Second %s, Third %s' %('hi',"two",3)
print 'First: {x} Second: {y} Third: {x}'.format(x = "inserted",y="two")
runfile('C:/Users/JoeRemote/.spyder/printFormats.py', wdir='C:/Users/JoeRemote/.spyder')
my_list = [1,2,3]
print my_list[0]
my_list = [1,"string",true]
my_list = [1,"string","true"]
len(my_list)
my_list = ["one","two","three",4,5]
my_list[0]
my_list[0:]
my_list[1:]
my_list[:-1]
my_list[:3]
my_list+["new","list"]
my_list*2
my_list**2
l = [1,2,3]
l.append(4)
l
print(l.pop())
print(l.sort())
l
x = l.pop(2)
x
l
l[4]
try:
    l[4]
new_list = ['a','e','x','b','c']
new_list.reverse()
new_list
new_list.sort()
new_list
l_1  = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = [l_1,l_2,l_3]
matrix
matrix[0]
matrix[0][2]
matrix[1][1]
first_col = [row[0] for row in matrix]
first_col
l = [1,2,4]
l[0]
my_dict = {'key':'value','key2':'value2'}
my_dict
my_dict[0]
my_dict[key]
my_dict['key']
my_dict = {'k1':123,'k3':3.5,'k4':"stringy"}
my_dict['k1']
my_dict['k1'] -120
my_dict = my_dict['k1'] -120
my_dict
d['animal']
d['animal'] = 'dog'
d = {}

d['animal'] = 'dog'
d['animal']
d= {'k1': {'nesty':{'subnesty':'value'}}}
d['k1']
d['k1']['nesty']
d['k1']['nesty']['subnesty']
d['k1']['nesty']['subnesty'].upper()
d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
d.keys()
d.values()
d.has_key('k1')
d.items()
d.update('k1',"hello")
t  = (1,2,3)

len(t)
t = ('one',2)
t[0]
t[1]
t[:-1]
t.index()
t.index('one')
t.count()
t.count('one')
pwd
f = open('myFile.txt')
f.read()
f.seek(0)
f.read()
f.seek(0)
f.readlines()
%%writefile new.txt
First Line
Second Line
for line in open('new.txt'):
    print(line)
x = set()
x.add(1)
x
x.add(2)
x
x.add(1)
x
l = [1,1,1,2,2,3,3,4]
set(l)
2=3
2==3
2===3
a = true
a
a = true
a = True
1>2
b = None
b
b = "A"
b = "B"
b == "A"

## ---(Sat Dec 16 17:58:55 2017)---
1==1
2!=1
2 <> 1
1<4
2<4<5
2 < 5 and 2<5
2 > 5 or 2>1 
 a = 2
b = 3

if a > b:
    a=2
else:
    b=4



print a
print b
 a = 2
b = 3

if a > b:
    a=4
else:
    b=4



print a
print b
if a > b:
    print "a is bigger"
elif b < a:
    print "b is bigger"
else a ==b: 
    print "they are equal"
if a > b:
    print "a is bigger"
elif b < a:
    print "b is bigger"
else a == b: 
    print "they are equal"
if a > b:
    print "a is bigger"
elif b < a:
    print "b is bigger"
else: 
    print "they are equal"
print a
print b
if a > b:
    print "a is bigger"
elif a < b:
    print "b is bigger"
else: 
    print "they are equal"
l = [1,2,3,4,5]

for element in l:
    sum += element


print sum
l = [1,2,3,4,5]
for element in l:
    sum+= element
for element in l:
    sum = sum + element


print sum
sum = 0
for element in l:
    sum = sum + element


print sum
for nums in l:
    if nums % 2 == 0:
        print "I am event
for nums in l:
    if nums % 2 == 0:
        print "I am even"
for element in l:
    sum += element


print sum
sum = 0
for element in l:
    sum += element


print sum
for item in s:
    print item
s = 'this is a string!'

for item in s:
    print item
s = 'this is a string!'

for letter in s:
    print item
s = 'this is a string!'

for letter in s:
    print letter
tup = (1,2,3,4,5)

for num in tup:
    print tup
tup = (1,2,3,4,5)

for num in tup:
    print t
tup = (1,2,3,4,5)

for num in tup:
    print num
l = [(2,4),(6,8),(10,12)]
l[0]
for tup in l:
    print tup
for (t1,t2) in l:
    print(t1)
d = {'k1': 1, 'k2': 2,'k3':3}
for item in d: 
    print item
for k,v in d.items():
    print k
    print v
x = 0

while x < 10:
    #do some code
    print 'x is currently: !',x
    x+= 1
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
x = 0

while x < 10:
    print 'x is currently: ,x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    
    if x==3:
        print ' Hey x equals 3!'
    else print 'Continuing . . '
    continue
x = 0

while x < 10:
    print 'x is currently: ' ,x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    
    if x==3:
        print ' Hey x equals 3!'
    else print 'Continuing . . '
    continue
x = 0

while x < 10:
    print 'x is currently: ' ,x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    
    if x==3:
        print ' Hey x equals 3!'
    else:
        print 'Continuing . . '
    continue
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
range(0,10)
range(0,10[2])
range(0,10,2)
x
x = range(0,10,2)

x
type(x)
for x in range(0,20):
    print(x)
l = []
for letter in 'word':
    l.append(letter)


print l
l = []
l = [letter for letter in 'word']
print l
lst = [x**2 for x in range(0,11)]
print lst
print lst

lst = [number for number in range(11) if number % 2 == 0]
print lst
celsius = [0,10,20.1,34.5]
fahrenheit = [ (temp*(9/5.0) + 32 ) for temp in celsius]
fahrenheit
lst = [ x**2 for x in [ x**2 for x in range(11)] ]

lst
l = [1,2,3,4,5]
l.append(6)
l = [1,2,3,4,5]
l.append(6)
l
def printName():
    print "hi Joe"
printName()
def printVariables(x,y):
    print 'Number 1: %s Number 2: %s',%x,%y
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
is_prime(13)
is_prime(12)
def square(num):
    result = num**2
    return result
square(2)
def square(num):
    return num**2

square(2)
def square(num):
    return num**2

square(3)
lambda num: num**2
square = lambda num: num**2
square(10)
even = lambda num: num%2==0
even(3)
lambda s: s[0]
first = lambda s: s[0]

first[0]
first('hello')
adder = lambda x,y: x+y
adder(2,10)
from __future__ import print_function
from IPython.display import clear_output
def display_board(board):
    
    clear_output()
    print('\t|\t|')
    print('--|--|--)
    print('\t|\t|')
    print('--|--|--)
    print('\t|\t|')
    pass
def display_board(board):
    
    clear_output()
    print('\t|\t|')
    print('--|--|--')
    print('\t|\t|')
    print('--|--|--')
    print('\t|\t|')
display_board()
display_board(1)
def display_board(board):
    
    clear_output()
    print('    |    |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('\t|\t|')
    print('--|--|--')
    print('\t|\t|')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('\t|\t|')
    print('--|--|--')
    print('\t|\t|')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('------------')
     print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('------------')
     print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')
    print('------------')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')
    print('------------')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('----------------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('----------------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')
    print('----------------------')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('-------------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('-------------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')
    print('-------------------')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')
board = ['anything','X','O','X','O','X','X','X','O','O']
display_board(board)
def player_input():
    
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
player_input()
choose_first()
def choose_first():
    return random.randint(1,2)
choose_first()
def choose_first():
    if random.randint(1,2) ==0:
        return 'Player 1'
    else: 
        return 'Player 2'
choose_first()
import random
choose_first()
runfile('C:/Users/JoeRemote/.spyder/TicTacToe.py', wdir='C:/Users/JoeRemote/.spyder')
"""
Created on Sat Dec 16 19:18:22 2017

@author: JoeRemote
"""

from __future__ import print_function
from IPython.display import clear_output
 import random  

def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('-----------------') 
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')





def player_input():
    
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')



def place_marker(board,marker,position):
    
    board[position] = marker


def win_check(board,mark):
    return ( (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[8] == mark and board[5] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark))


def choose_first():
    if random.randint(1,2) ==0:
        return 'Player 1'
    else: 
        return 'Player 2'



def space_check(board,position):
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True




def player_choice(board):
    
    position  = ' ' 
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)


def replay():
    return raw_input('Do you want to play again? Enter Yes or No').lower().startswith('y')



print ('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + ' will go first')
    
    game_on = True
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_markert):
                display_board(theBoard)
                print('Congratulations, Player 1, has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else: 
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_markert):
                display_board(theBoard)
                print('Congratulations, Player 2, has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else: 
                    turn = 'Player 1'
    
    if not replay():
        break
runfile('C:/Users/JoeRemote/.spyder/TicTacToe.py', wdir='C:/Users/JoeRemote/.spyder')
"""
Created on Sat Dec 16 19:18:22 2017

@author: JoeRemote
"""

from __future__ import print_function
from IPython.display import clear_output
import random  

def display_board(board):
    
    clear_output()
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
    print('     |     |')
    print('-----------------') 
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )
    print('     |     |')





def player_input():
    
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')



def place_marker(board,marker,position):
    
    board[position] = marker


def win_check(board,mark):
    return ( (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[8] == mark and board[5] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark))


def choose_first():
    if random.randint(1,2) ==0:
        return 'Player 1'
    else: 
        return 'Player 2'



def space_check(board,position):
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True




def player_choice(board):
    
    position  = ' ' 
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)


def replay():
    return raw_input('Do you want to play again? Enter Yes or No').lower().startswith('y')



print ('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + ' will go first')
    
    game_on = True
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations, Player 1, has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else: 
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations, Player 2, has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else: 
                    turn = 'Player 1'
    
    if not replay():
        break
runfile('C:/Users/JoeRemote/.spyder/Classes.py', wdir='C:/Users/JoeRemote/.spyder')
class Sample(object):
    pass


x = Sample()
type(x)
class Dog(object):
    
    def __init__(self, breed):
        self.breed= breed
sam = Dog(breed='lab')
sam.breed
class Dog(object):
    
    
    #Class object attribute
    #no matter what object we make, the species will be a mammal
    species = 'mammal'
    
    #should always be the first method
    #always start with self in the parameters
    def __init__(self, breed):
        self.breed= breed
sam.species
class Dog(object):
    
    
    #Class object attribute
    #no matter what object we make, the species will be a mammal
    species = 'mammal'
    
    #should always be the first method
    #always start with self in the parameters
    def __init__(self, breed,name):
        self.breed= breed
        self.name = name


sam = Dog(breed='lab',name = 'sam')
sam.breed
sam.species
sam.breed
sam.species
sam.name
sam.breed
sam.species
sam.name
def print_string():
    print self.name + 'is a ' self.breed
class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self):
        pass
class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius



c = Circle()
c.pi
class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius



c = Circle(radius =100)
c.pi
c.radius
class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        #radius**2 * pi
        return (self.radius**2) * pi
class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        #radius**2 * pi
        return (self.radius**2) * self.pi
class Circle(object):
    
    #class object attributes
    
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi
c = Circle(radius =100)
c.area()
def set_radius(self,new_radius):
    self.radius = new_radius
c.set_radius(50)
c.area()
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
c = Circle(radius =100)
c.pi
c.radius
c.area()
c.set_radius(50)
c.area()
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
c.get_radius()
class Animal(object):
    
    def __init__(self):
      print 'Animal Created'
class Animal(object):
    
    def __init__(self):
      print "Animal Created"
    
    
    def whoAmI(self):
        print "Animal"
    def eat(self):
        print "Eating"


class Dog(Animal):
    
    
    def __init__(self):
        Animal.__init__(self)
        print "Dog Created"
    
    def whoAmI(self):
        print "Dog"
    
    def bark(self):
        print "Woof"
lass Animal(object):
    
    def __init__(self):
      print "Animal Created"
    
    
    def whoAmI(self):
        print "Animal"
    def eat(self):
        print "Eating"
class Animal(object):
    
    def __init__(self):
      print "Animal Created"
    
    
    def whoAmI(self):
        print "Animal"
    
    def eat(self):
        print "Eating"
class Animal(object):
    
    def __init__(self):
      print("Animal Created")
class Animal(object):
    
    def __init__(self):
      print("Animal Created")
    
    
    def whoAmI(self):
        print "Animal"
    
    def eat(self):
        print "Eating"
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
d.whoAmI()
d.eat()
d.bark()
l = [1,2,3]

print l
l = [1,2,3]

print( l)
class Book(object):
    
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        print("A book has been created")
b = Book('Python','Jose',100)
print(b)
class Book(object):
    
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        print("A book has been created")
    
    def __str__(self):
        return "Title: %s, Author: %s, pages %s " %(self.title,self.author,self.pages)
b = Book('Python','Jose',100)

print(b)
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
len(b)
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


b = Book('Python','Jose',100)

len(b)
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
del b
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
try:
   2 + 's'
except TypeError:
    print "There was a type Error"
try:
   2 + 's'
except TypeError:
    print("There was a type Error")
try: 
    f = open('testfile','r')
    f.write('Test write this ')
except:
    print('Error in writing to the file!')

else: 
    print('File write was a succcess')
"else statements within the Try"
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
    try:
        val = int(input('Please enter an integer: '))
    except:
        print('Looks like you did not enter and integer!')
    finally:
        print('Finally Executed')
    print val
askint()
def askint():
    try:
        val = int(input('Please enter an integer: '))
    except:
        print('Looks like you did not enter and integer!')
    finally:
        print('Finally Executed')
    print val


askint()
def askint():
    try:
        val = int(input('Please enter an integer: '))
    except:
        print('Looks like you did not enter and integer!')
    finally:
        print('Finally Executed')
    print(val)


askint()
def askint():
    
    try:
        val = int(input('Please enter an integer: '))
    except:
        print('Looks like you did not enter and integer!')
        val = int(raw_input("Try again - Please enter an integer"))
    finally:
        print('Finally Executed')
    print(val)


askint()
def askint():
    
    while True:
        
        try:
            val = int(input('Please enter an integer: '))
        except:
            print('Looks like you did not enter and integer!')
            continue
        else:
            print 'Correct, that is an integer!'
            break
        finally:
            print('Finally Executed')
        
        print(val)


askint()
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
runfile('C:/Users/JoeRemote/.spyder/BlackJack.py', wdir='C:/Users/JoeRemote/.spyder')
class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                cards.append(card)
                print(card)
deck = Deck()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = ()
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                print(card)
deck = Deck()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                print(card)



deck = Deck()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                print(card)



deck = Deck()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                print(card)
    
    def deal(self):
        return self.cards.pop()
lst = [ x**2 for x in [ x**2 for x in range(11)] ]

lst
cardIndex = [x for x in range(52)]
cardIndex
len(self.cards)
self.cards.count()
for x in range(51):
    print random.randint(0,51)
import random
for x in range(51):
    print random.randint(0,51)
for x in range(51):
    print random.random(0,51)
for x in range(51):
    print random.randint()
for x in range(51):
    print(random.randint())
for x in range(51):
    print(random.randint(0,51,1))
for x in range(51):
    print(random.randint(0,51))
range(51)
range(52)
random.randint(0,51)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if self.cards[51-nextIndex] in shuffled:
                     nextIndex -= 1
                     continue
                 else:
                     shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                     nextShuffledIndex -= 1
                     notStruck == True
                     break
        
        print(shuffled)




shuffle()
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print(shuffled)




d = Deck()
d.shuffle()
debugfile('C:/Users/JoeRemote/.spyder/BlackJack.py', wdir='C:/Users/JoeRemote/.spyder')
d.shuffle()
runfile('C:/Users/JoeRemote/.spyder/BlackJack.py', wdir='C:/Users/JoeRemote/.spyder')
d.shuffle()
def shuffle(self):
    #Write down all numbers 1 to N
    cardIndex = [x for x in range(52)]
    shuffled  = []
    nextShuffledIndex = 51
    
    #Do until shuffled deck has 52  cards     
    while shuffled.count != 52:
        #Get the next random index
         nextIndex = random.randint(0,51)
         #initialize a card not used Variable
         notStruck = False    
         
         
         while notStruck == False:
             if 51-nextIndex > 0:
                 if self.cards[51-nextIndex] in shuffled:
                     nextIndex -= 1
                     continue
                 else:
                     shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                     nextShuffledIndex -= 1
                     notStruck == True
                     break
    
    print(shuffled)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print(shuffled)




d = Deck()
d.shuffle()
%clear
runfile('C:/Users/JoeRemote/.spyder/BlackJack.py', wdir='C:/Users/JoeRemote/.spyder')
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print(shuffled)




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print(shuffled)
d = Deck()
d.shuffle()
print('deck length' + self.cards.count())
print('shuffled length' + shuffled.count())
cardIndex = [x for x in range(52)]
shuffled  = []
nextShuffledIndex = 51

print('deck length' + self.cards.count())
print('shuffled length' + shuffled.count())
def shuffle(self):
    #Write down all numbers 1 to N
    cardIndex = [x for x in range(52)]
    shuffled  = []
    nextShuffledIndex = 51
    
    print('deck length' + self.cards.count())
    print('shuffled length' + shuffled.count())
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        print('deck length' + self.cards.count())
        print('shuffled length' + shuffled.count())
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        print('deck length' + len(self.cards))
        print('shuffled length' + len(shuffled))
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        print('deck length %s' %(len(self.cards))
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        print('deck length %s' %(len(self.cards)))
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        cardIndex = [x for x in range(52)]
        shuffled  = []
        nextShuffledIndex = 51
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length%s' %(len(shuffled)))
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print(shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print(nextIndex)
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print(nextIndex)
                 
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         if nextIndex < 0:
                              nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print('The next index is %s' %s(nextIndex))
                 
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         if nextIndex < 0:
                              nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,51)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print('The next index is %s' %(nextIndex))
                 
                 if 51-nextIndex > 0:
                     if self.cards[51-nextIndex] in shuffled:
                         nextIndex -= 1
                         if nextIndex < 0:
                              nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print('The next index is %s' %(nextIndex))
                 
                 if 51-nextIndex > 0:
                     print('Next index is not negative')
                     if self.cards[51-nextIndex] in shuffled:
                         
                         nextIndex -= 1
                         if nextIndex < 0:
                              nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print('The next index is %s' %(nextIndex))
                 
                 if 51-nextIndex > 0:
                     print('Next index is not negative')
                     if self.cards[51-nextIndex] in shuffled:
                         
                         nextIndex -= 1
                         if nextIndex < 0:
                              nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        
        
        print('The shuffled deck:' + shuffled)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
             notStruck = False    
             
             
             while notStruck == False:
                 print('The next index is %s' %(nextIndex))
                 
                 if 51-nextIndex > 0:
                     print('Next index is not negative')
                     if self.cards[51-nextIndex] in shuffled:
                         
                         nextIndex -= 1
                         nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
print('shuffled  %s' %(shuffled))
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
             nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
             notStruck = False    
             
             
             #while notStruck == False:
                 print('The next index is %s' %(nextIndex))
                 
                 if (51-nextIndex) > 0:
                     print('Next index is not negative')
                     if self.cards[51-nextIndex] in shuffled:
                         print('The card is already shuffled')
                         nextIndex -= 1
                         nextIndex = random.randint(0,51)
                         continue
                     else:
                         shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                         nextShuffledIndex -= 1
                         notStruck == True
                         break
        
        
        
        print('The shuffled deck:' + shuffled)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[51-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                continue
            else:
                shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
                break
        
        
        
        print('The shuffled deck:' + shuffled)
def shuffle(self):
    #Write down all numbers 1 to N
    shuffled = [x for x in range(52)]
    nextShuffledIndex = 51
    
    
    
    print('deck length %s' %(len(self.cards)))
    print('shuffled length %s' %(len(shuffled)))
    print('shuffled  %s' %(shuffled))
    
    #Do until shuffled deck has 52  cards     
   # while shuffled.count != 52:
        #Get the next random index
    nextIndex = random.randint(0,nextShuffledIndex)
         #initialize a card not used Variable
    notStruck = False    
         
         
         #while notStruck == False:
    print('The next index is %s' %(nextIndex))
    
    if (51-nextIndex) > 0:
        print('Next index is not negative')
        if self.cards[51-nextIndex] in shuffled:
            print('The card is already shuffled')
            nextIndex -= 1
            nextIndex = random.randint(0,51)
            #continue
        else:
            shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
            nextShuffledIndex -= 1
            notStruck == True
           # break
    
    
    
    print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[51-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               # break
        
        
        
        print('The shuffled deck:' + shuffled)
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[51-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[51-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                print('The card will be added to shuffled')
                shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                print('The card will be added to shuffled')
                shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                print('The card will be added to shuffled')
                shuffled.remove(nextShuffledIndex)
                shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                print('The card will be added to shuffled')
                shuffled.remove(nextShuffledIndex)
                print('The card being added %s' %(self.cards[52-nextIndex])
                shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       # while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             #while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                #continue
            else:
                print('The card will be added to shuffled')
                shuffled.remove(nextShuffledIndex)
                print('The card being added %s' %(self.cards[52-nextIndex]))
                shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
               
               # break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       while shuffled.count != 52:
            #Get the next random index
        nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
        notStruck = False    
             
             
             while notStruck == False:
        print('The next index is %s' %(nextIndex))
        
        if (51-nextIndex) > 0:
            print('Next index is not negative')
            if self.cards[52-nextIndex] in shuffled:
                print('The card is already shuffled')
                nextIndex -= 1
                nextIndex = random.randint(0,51)
                continue
            else:
                print('The card will be added to shuffled')
                shuffled.remove(nextShuffledIndex)
                print('The card being added %s' %(self.cards[52-nextIndex]))
                shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                nextShuffledIndex -= 1
                notStruck == True
                
                break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
       while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            
            
            while notStruck == False:
                print('The next index is %s' %(nextIndex))
                
                if (51-nextIndex) > 0:
                    print('Next index is not negative')
                    if self.cards[52-nextIndex] in shuffled:
                        print('The card is already shuffled')
                        nextIndex -= 1
                        nextIndex = random.randint(0,51)
                        continue
                    else:
                        print('The card will be added to shuffled')
                        shuffled.remove(nextShuffledIndex)
                        print('The card being added %s' %(self.cards[52-nextIndex]))
                        shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                        nextShuffledIndex -= 1
                        notStruck == True
                        break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            
            
            while notStruck == False:
                print('The next index is %s' %(nextIndex))
                
                if (51-nextIndex) > 0:
                    print('Next index is not negative')
                    if self.cards[52-nextIndex] in shuffled:
                        print('The card is already shuffled')
                        nextIndex -= 1
                        nextIndex = random.randint(0,51)
                        continue
                    else:
                        print('The card will be added to shuffled')
                        shuffled.remove(nextShuffledIndex)
                        print('The card being added %s' %(self.cards[52-nextIndex]))
                        shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                        nextShuffledIndex -= 1
                        notStruck == True
                        break
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[52-nextIndex] in shuffled:
                    print('The card is already shuffled')
                    nextIndex -= 1
                    nextIndex = random.randint(0,51)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s' %(self.cards[52-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            
            if (52-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[52-nextIndex] in shuffled:
                    print('The card is already shuffled')
                    nextIndex -= 1
                    nextIndex = random.randint(0,51)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s' %(self.cards[52-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[52-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    nextIndex -= 1
                    nextIndex = random.randint(0,51)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[52-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[52-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    nextIndex -= 1
                    nextIndex = random.randint(0,51)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[52-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    nextIndex -= 1
                    nextIndex = random.randint(0,51)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[52-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    nextIndex -= 1
                    nextIndex = random.randint(0,51)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    nextIndex -= 1
                    nextIndex = random.randint(0,nextShuffledIndex)
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while shuffled.count != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
             #initialize a card not used Variable
            notStruck = False    
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   notStruck == True
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                    continue
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] in shuffled:
                    print('The card is already shuffled\n')
                
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))
d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                    print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                if self.cards[51-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        print('The shuffled deck: %s'%(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        print(for x in self.cards)




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        for x in self.cards:
            print x




d = Deck()
d.shuffle()
class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        for x in self.cards:
            print(x)




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex] not in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        
        for x in shuffled:
            print(x)




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex]  in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                
                else:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex]  in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                
                elif self.cards[nextShuffledIndex-nextIndex]  not in shuffled:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex]   in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will be added to shuffled')
                
                elif self.cards[nextShuffledIndex-nextIndex]  not in shuffled:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                if self.cards[nextShuffledIndex-nextIndex]   in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will is in the shuffled')
                
                elif self.cards[nextShuffledIndex-nextIndex]  not in shuffled:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                print('The index of the card in the shuffled list is %s' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                if self.cards[nextShuffledIndex-nextIndex]   in shuffled:
                    #print('The card is already shuffled\n')
                   print('The card will is in the shuffled')
                
                elif self.cards[nextShuffledIndex-nextIndex]  not in shuffled:
                   print('The card will be added to shuffled')
                   shuffled.remove(nextShuffledIndex)
                   print('The card being added %s\n' %(self.cards[51-nextIndex]))
                   shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                   nextShuffledIndex -= 1
                   cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (51-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (nextShuffledIndex-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[nextShuffledIndex-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[nextShuffledIndex-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[nextShuffledIndex-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[nextShuffledIndex-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[52-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[52-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[51-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,52)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,52)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 51
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            
            print('The next index is %s'%(nextIndex))
            if (52-nextIndex) > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            deckIndexToRemove = 52-nextIndex
            print('The next index is %s'%(nextIndex))
            if deckIndexToRemove > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            deckIndexToRemove = 52-nextIndex
            print('The next index is to be removed %s'%(deckIndexToRemove))
            if deckIndexToRemove > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[nextShuffledIndex-nextIndex])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        #Do until shuffled deck has 52  cards     
        while cardsAdded != 52:
            #Get the next random index
            nextIndex = random.randint(0,nextShuffledIndex)
            deckIndexToRemove = 52-nextIndex
            print('The next index is to be removed %s'%(deckIndexToRemove))
            if deckIndexToRemove > 0:
                
                print('Next index is not negative')
                print('The next card is %s' %(self.cards[nextShuffledIndex-nextIndex]))
                try:
                    
                    print('The index of the card in the shuffled list is %s\n' %(shuffled.index(self.cards[deckIndexToRemove])))
                
                except:
                      print('The card will be added to shuffled')
                      shuffled.remove(nextShuffledIndex)
                      print('The card being added %s\n' %(self.cards[51-nextIndex]))
                      shuffled.insert(nextShuffledIndex,self.cards[51-nextIndex])
                      nextShuffledIndex -= 1
                      cardsAdded += 1
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()
d.shuffle()
d = Deck()
d.cards
for x in d.cards:
    print(x)
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(1,53)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i-1)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i-1)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        for x in shuffled:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        for x in self.cards:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
          
          for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        for x in self.cards:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
         
         for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        for x in self.cards:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        nextShuffledIndex = 52
        cardsAdded = 0
        
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        for x in self.cards:
            print(x)
        
        print(len(shuffled))




d = Deck()

d.shuffle()
runfile('C:/Users/JoeRemote/.spyder/BlackJack.py', wdir='C:/Users/JoeRemote/.spyder')
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print("Current Hand: %s") %(self.player.currentHand())
newGame = Game()

Game.start()
newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print("Current Hand: %s") %(self.player.current_Hand())






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print("Current Hand: %s") %(self.player.current_hand())






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print("Current Hand: %s") %(self.player.hand))






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print "Current Hand: %s") %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        print "Current Hand: %s", %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        
        #Do some more stuff here
        
        cardToBeDealt = self.deck.deal()
        
        
        for i in range(2):
            self.player.hand.callForCard(cardToBeDealt)
        
        
        for i in range(2):
            self.dealer.hand.callForCard(cardToBeDealt)
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()

print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in card:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()

print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in cards:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()

print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + card 
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()

print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + (str)card
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()

print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()

print(newGame.player.hand)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand())
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
        
        print('deck length %s' %(len(self.cards)))
        print('shuffled length %s' %(len(shuffled)))
        print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        #for i in range(2):
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def start(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.start()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            print("dealer: " + str(self.dealer.current_hand()))
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.player.hand.callForCard(cardToBeDealt)
            print("player: " + str(self.player.current_hand()))
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.player.hand.callForCard(cardToBeDealt)
            print("Current Hand: " + str(self.player.current_hand()))
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.player.hand.callForCard(cardToBeDealt)
        
        print("Current Hand: " + str(self.player.current_hand()))
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
           
           for b in range(2):
            cardToBeDealt = self.deck.deal()
            self.player.hand.callForCard(cardToBeDealt)
        
        print"Current Hand: " + str(self.player.current_hand())
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        print"Current Hand: " + str(self.player.current_hand())
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        print("Current Hand: " + str(self.player.current_hand()))
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()

print("Current Hand: " + str(newGame.player.current_hand()))
print("Current Pot: " + str(newGame.player.bankRoll))
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()

print("Current Hand: " + str(newGame.player.current_hand()))
print("Current Pot: $" + str(newGame.player.bankRoll))
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()

print("Current Hand: " + str(newGame.player.current_hand()))
print("Current Pot: $" + str(newGame.player.bankRoll))
newGame.bet = input("Place your bet: ")
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()

newGame.play()

print("Current Hand: " + str(newGame.player.current_hand()))
print("Current Pot: $" + str(newGame.player.bankRoll))
newGame.bet = input("Place your bet: ")
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPlaying
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = input("Bet(b) or Fold(f): ") 
    if betOrFold == 'b':
        newGame.bet = input("Place your bet: ")
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPlaying:
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = input("Bet(b) or Fold(f): ") 
    if betOrFold == 'b':
        newGame.bet = input("Place your bet: ")
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = input("Bet(b) or Fold(f): ") 
    if betOrFold == 'b':
         while True:
            
            try:
                newGame.bet = int(input("Place your bet: "))
            except:
                print('That is not a valid bet, Try Again!')
                continue
    
    else:
        break
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = input("Bet(b) or Fold(f): ") 
    
    if betOrFold == 'b':
         while True:
            
            try:
                newGame.bet = int(input("Place your bet: "))
            except:
                print('That is not a valid bet, Try Again!')
                continue
    
    else:
        break
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = str(input("Bet(b) or Fold(f): ")) 
    
    if betOrFold == 'b':
         while True:
            
            try:
                newGame.bet = int(input("Place your bet: "))
            except:
                print('That is not a valid bet, Try Again!')
                continue
    
    else:
        break
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = str(input("Bet(b) or Fold(f): ")) 
    print(betOrFold)
    if betOrFold == 'b':
         while True:
            
            try:
                newGame.bet = int(input("Place your bet: "))
            except:
                print('That is not a valid bet, Try Again!')
                continue
    
    else:
        break
even = lambda num: num%2==0
even(3)
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    bet = lambda:  str(input("Bet(b) or Fold(f): ")) =='b'
   
   while True:
       
       try:
           newGame.bet = int(input("Place your bet: "))
       except:
           print('That is not a valid bet, Try Again!')
           continue
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    bet = lambda:  str(input("Bet(b) or Fold(f): ")) =='b'
    
    while True:
       
       try:
           newGame.bet = int(input("Place your bet: "))
       except:
           print('That is not a valid bet, Try Again!')
           continue
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    
    while True:
       
       try:
           newGame.bet = int(input("Place your bet: "))
           break
       except:
           print('That is not a valid bet, Try Again!')
           continue
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
    betOrFold = input("Bet(b) or Fold(f): ")
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'Kking':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        #print(Card)
    
    
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)






newGame = Game()
isPLaying = True
while isPLaying :
    
    newGame.play()
    
    
    while True:
       
       try:
           newGame.bet = int(input("Place your bet: "))
           if newGame.bet < newGame.player.bankRoll and newGame.bet > 0 :
               break
           else:
               print('Invalid bet, you only have ' + str(newGame.player.bankRoll) + ' remaining')
       except:
           print('That is not a valid bet, Try Again!')
           continue
    
    print("Current Hand: " + str(newGame.player.current_hand()))
    print("Current Pot: $" + str(newGame.player.bankRoll))
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
        self.ace = False
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        random.shuffle(self.cards)
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        
        
        while isPLaying :
            
            newGame.play()
            
            
            while True:
               
               try:
                   newGame.bet = int(input("Place your bet: "))
                   if newGame.bet <= newGame.player.bankRoll and newGame.bet > 0 :
                       if newGame.bet == newGame.player.bankRoll:
                           print('Going all in!')
                       break
                   else:
                       print('Invalid bet, you only have ' + str(newGame.player.bankRoll) + ' remaining')
               except:
                   print('That is not a valid bet, Try Again!')
                   continue
            
            print("Current Hand: " + str(newGame.player.current_hand()))
            print("Current Pot: $" + str(newGame.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        random.shuffle(self.cards)
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        
        
        while isPLaying :
            
            newGame.play()
            
            
            while True:
               
               try:
                   newGame.bet = int(input("Place your bet: "))
                   if newGame.bet <= newGame.player.bankRoll and newGame.bet > 0 :
                       if newGame.bet == newGame.player.bankRoll:
                           print('Going all in!')
                       break
                   else:
                       print('Invalid bet, you only have ' + str(newGame.player.bankRoll) + ' remaining')
               except:
                   print('That is not a valid bet, Try Again!')
                   continue
            
            print("Current Hand: " + str(newGame.player.current_hand()))
            print("Current Pot: $" + str(newGame.player.bankRoll))







newGame = Game()
newGame.play()
lst = [ x**2 for x in [ x**2 for x in range(11)] ]

lst
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        random.shuffle(self.cards)
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 newGame.bet = int(input("Place your bet: "))
                 if newGame.bet <= newGame.player.bankRoll and newGame.bet > 0 :
                     if newGame.bet == newGame.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(newGame.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
            
            print("Current Hand: " + str(newGame.player.current_hand()))
            print("Current Pot: $" + str(newGame.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        random.shuffle(self.cards)
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
            
            print("Current Hand: " + str(self.player.current_hand()))
            print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        random.shuffle(self.cards)
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
            
            print("Current Hand: " + str(self.player.current_hand()))
            print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
            
            print("Current Hand: " + str(self.player.current_hand()))
            print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
            
            print("Current Hand: " + str(self.player.current_hand()))
            print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        isPLaying = True
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                        break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           print(self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' + str(self.dealer.hand.show(hidden=True)))
        
        hitOrStand






newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           print(self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' + str(self.dealer.hand.show(hidden=True)))








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           print(self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()

## ---(Tue Dec 19 13:59:04 2017)---
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           print(self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        print( "%s of %s" %(self.rank, self.suit))



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" + card
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        print( "%s of %s" %(self.rank, self.suit))



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        print( "%s of %s" %(self.rank, self.suit))



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll))
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: \n"))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("Current Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
           self.cards[x]


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)








newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)
        
        if playing == False:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.value + 10
        else:
            return self.value
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)
        
        if self.playing == False:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)
        
        if self.playing == False:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def deal_cards(self):
        #Deal
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
    
    
    
    def play(self):
        
        
        
        #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        self.deal_cards()
        #print "Current Hand: %s" %(self.player.hand)
        
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
        
        self.player.bankRoll-= self.bet
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)
        
        if self.playing == True:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))







newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
        self.result = ''
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    def set_bet(self,bet):
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
    
    def deal_cards(self):
        #Deal
           
           
           #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        
        self.set_bet()
        
        
        
        if self.playing == True:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))
            self.player.bankRoll-= self.bet
        
        self.playing = True
    
    
    
    def play(self):
        
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)










newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
        self.result = ''
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def set_bet(self,bet):
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
    
    def deal_cards(self):
        #Deal
           
           
           #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        
        
        
        
        
        if self.playing == True:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))
            self.player.bankRoll-= self.bet
        
        self.playing = True
    
    
    
    def play(self):
        
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)










newGame = Game()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
        self.result = ''
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def set_bet(self,bet):
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
    
    def deal_cards(self):
        #Deal
           
           
           #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        
        
        
        
        
        if self.playing == True:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))
            self.player.bankRoll-= self.bet
        
        self.playing = True
    
    
    
    def play(self):
        
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)










newGame = Game()
newGame.deal_cards()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
        self.result = ''
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def set_bet(self,bet):
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
    
    def deal_cards(self):
        #Deal
           
           
           #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        
        self.set_bet()
        
        
        
        if self.playing == True:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))
            self.player.bankRoll-= self.bet
        
        self.playing = True
    
    
    
    def play(self):
        
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)










newGame = Game()
newGame.deal_cards()
newGame.play()
"""
Created on Sun Dec 17 11:53:14 2017

Black Jack Game

@author: JoeRemote
"""

import random

class BasePlayer(object):
    
    
    def __init__(self):
        self.isBusted = False
    
    
    def current_hand(self):
        hand = Hand()
        #Find out if hand is busted
        return hand


class Player(BasePlayer):
    
    
    
    def __init__(self):
        self.bankRoll = 100
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand
    
    def hit(self):
        self.hand.callForCard()
    
    
    def stand(self):
        
        pass


class Dealer(BasePlayer):
    
    def __init__(self):
        self.hand = Hand()
    
    def current_hand(self):
        
        return self.hand



class Hand(object):
    
    def __init__(self):
        self.cards = []
        self.total = 0
        self.ace = False
        # Point values dict (Note: Aces can also be 11, check self.ace for details)
        self.card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    
    def callForCard(self,Card):
        self.cards.append(Card)
        
        if Card.rank == 'Ace':
            self.ace = True
        self.total += self.card_val[Card.rank]
        #print(Card)
    
    def calc_val(self):
        if(self.ace and self.total <12):
            return self.total + 10
        else:
            return self.total
    def __str__(self):
        stringHand = ''
        for card in self.cards:
            stringHand +=  "|" +str(card)
        
        return stringHand
    
    def show(self,hidden):
        if hidden:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
          print( self.cards[x])


class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "%s of %s" %(self.rank, self.suit)



class Deck(object):
    
    
    
    def __init__(self):
        suits = ['Hearts','Clubs','Diamonds','Spades']
        ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)
                #print(card)
    
    def deal(self):
        return self.cards.pop()
    
    def shuffle(self):
        #Write down all numbers 1 to N
        shuffled = [x for x in range(0,52)]
       
       # print('deck length %s' %(len(self.cards)))
        #print('shuffled length %s' %(len(shuffled)))
        #print('shuffled  %s' %(shuffled))
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        for i in shuffled:
            j = random.randint(0,i)
            #print(j)
            tmpCard = self.cards[j]
            self.cards[j] = self.cards[i]
            self.cards[i] = tmpCard
        
        
        
        
        
        
        
        
        #for x in self.cards:
           #print(x)
        
        #print(len(shuffled))








class Game(object):
    
    #Constructor
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = 0
        self.playing = False
        self.result = ''
    
    
    #Get Functions
    def get_deck(self):
        return self.deck
    
    def get_dealer(self):
        return self.dealer
    
    def get_player(self):
        return self.player
    
    def get_bet(self):
        return self.bet
    
    def set_bet(self):
        while True:
            
            try:
                 self.bet = int(input("Place your bet: "))
                 if self.bet <= self.player.bankRoll and self.bet > 0 :
                     if self.bet == self.player.bankRoll:
                        print('Going all in!\n')
                     break
                 else:
                     print('Invalid bet, you only have ' + str(self.player.bankRoll) + ' remaining')
            except:
                 print('That is not a valid bet, Try Again!')
                 continue
    
    def deal_cards(self):
        #Deal
           
           
           #Welcome to the game
        print("\n\n\tWelcome to Blackjack!")
        
        print("")
        self.deck.shuffle()
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.dealer.hand.callForCard(cardToBeDealt)
            #print("dealer: " + str(self.dealer.current_hand()))
        
        for b in range(2):
           cardToBeDealt = self.deck.deal()
           self.player.hand.callForCard(cardToBeDealt)
        
        
        self.set_bet()
        
        
        
        if self.playing == True:
            print('--- for a total of ' + str(self.dealer.hand.calc_val()))
            self.player.bankRoll-= self.bet
        
        self.playing = True
    
    
    
    def play(self):
        
        print("\nCurrent Hand: " + str(self.player.current_hand()))
        print("Current Hand Value: " + str(self.player.hand.total))
        print("Current Pot: $" + str(self.player.bankRoll) + '\n')
        
        print('Dealers hand: ' )
        self.dealer.hand.show(hidden=True)










newGame = Game()
newGame.deal_cards()
newGame.play()