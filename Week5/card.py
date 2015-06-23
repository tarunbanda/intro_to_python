"""
    card.py
    Defines class card. 
    Tarun Banda
    Python Assignment 5
"""

class Card:
        
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit


    def getRank(self):
        cardRank = {1:'Ace', 2: "Two", 3: "Three", 4:"Four", 
                4: "Five", 6:"Six", 7:"Seven", 8:"Eight", 
                9:"Nine", 10:"Ten",11: "Jack",12:"Queen",13: "King"}
        return cardRank[self.rank]

            
    def getSuit(self):
        cardSuit = {"d": "Diamonds", "c" : "Clubs","h" : "Hearts","s":"Spades"}
        return cardSuit[self.suit]
    
        
    def bjValue(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank


    #
    def __str__(self):
        cardRank = {1:'Ace', 2: "Two", 3: "Three", 4:"Four", 
                4: "Five", 6:"Six", 7:"Seven", 8:"Eight", 
                9:"Nine", 10:"Ten",11: "Jack",12:"Queen",13: "King"}
        cardSuit = {"d": "Diamonds", "c" : "Clubs","h" : "Hearts","s":"Spades"}
        return "%s of %s" % (cardRank[self.rank],cardSuit[self.suit])

