"""
    testCard.py
    Tests class card. 
    Tarun Banda
    Python Assignment 5
"""

import card

c = card.Card(4,"h") #Passes Card the variables 4 and 'h"
#print each of the methods of class card
print (c)
print c.getRank()
print c.getSuit()
print c.bjValue()


##=====================OUTPUT===================================================
#===============================================================================
#c = card.Card(1,"s")
# Ace of Spades
# Ace
# Spades
# 1
#
#c = card.Card(11, "d")
#Jack of Diamonds
#Jack
#Diamonds
#10
#
#
#c = card.Card(13, "c")
#King of Clubs
#King
#Clubs
#10
#
#
#c = card.Card(4, "h")
#Five of Hearts
#Five
#Hearts
#4
#===============================================================================
