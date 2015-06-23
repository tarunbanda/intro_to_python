"""
    cards.py
    Defines class cards. 
"""

class Card:
    '''
        One object of class Card stores one cards's rank and suit
    '''        
    
    def __init__(self,rank,suit):
        '''
            Card constructor, excecuted every time a new Card object is created
            raise TypeErrors and ValueErrors when needed
        '''
            
        if type(rank) != int or type(suit) != str:
            raise TypeError() #raises TypeError when rank isn't an int or suit isn't a string
        if rank > 13 or rank < 1:
            raise ValueError() #raises a value error when value of rank is not in between 1 and 13
        if suit != ('s' or 'h' or 'c'or 'd' ):
            raise ValueError() # raises value error when string enter in suit doesn't match ('s' or 'h' or 'c'or 'd' )
        self.rank = rank #initializing rank if no errors
        self.suit = suit #initializing suit if no errors


    def getRank(self):
        '''
            returns the rank of a cards using dictionary cardRank
        '''
        # Dict cardRank stores strings for each int rank
        cardRank = {1:'Ace', 2: "Two", 3: "Three", 4:"Four", 
                5: "Five", 6:"Six", 7:"Seven", 8:"Eight", 
                9:"Nine", 10:"Ten",11: "Jack",12:"Queen",13: "King"}
        return (cardRank[self.rank]) 

            
    def getSuit(self):
        '''
            returns the suit of a cards using dictionary cardSuit
        '''
        #Dict cardSuit has key:value pairs for each suit
        cardSuit = {"d": "Diamonds", "c" : "Clubs","h" : "Hearts","s":"Spades"}
        return (cardSuit[self.suit])
    
        
    def bjValue(self):
        '''
            bjValue returns the blackjack value of the cards
        '''
        # if statement to return 10 when cards is a face cards
        if self.rank > 10:
            return 10
        else:
            return (self.rank)


    #
    def __str__(self):
        '''
            Converts Card object into a string and returns proper cards and rank
        '''
        cardRank = {1:'Ace', 2: "Two", 3: "Three", 4:"Four", 
                5: "Five", 6:"Six", 7:"Seven", 8:"Eight", 
                9:"Nine", 10:"Ten",11: "Jack",12:"Queen",13: "King"}
        
        cardSuit = {"d": "Diamonds", "c" : "Clubs","h" : "Hearts","s":"Spades"}
        
        return "%s of %s" % (cardRank[self.rank],cardSuit[self.suit])




        