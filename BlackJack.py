# -*- coding: utf-8 -*-
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
  

 