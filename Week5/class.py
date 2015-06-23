"""
	Defines class card. 
"""

class Card:

	def __init__(self):
		self.rank = 0
		self.suit = 0

	def getRank(self,rank):
		self.rank = rank

	def getSuit(self,suit):
		self.suit = suit

	#def bjValue(self):


	#
	def __str__(self):
		return "%i of %i" % (self.rank,self. self.suit)


c = card(1, 2)
print (c)