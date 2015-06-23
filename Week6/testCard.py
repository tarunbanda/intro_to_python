
'''
    Test Card class for type and value errors
'''
import card #imports card class



try: #test TypeError where rank = string
    c = card.Card('e', 's') 
except:
    print ("Can't use a string in the rank field")


try: #test ValueError were rank is outside or range 1-13
    c = card.Card(14,'s')
except:
    print("Can't use a number outside the range of 1-13")
    
try: #test TypeError when suit != string
    c = card.Card(2,2)
except:
    print("Must use string for suit")
    
try: #test ValueError when suit != ('s', 'h', 'c', 'd')
    c = card.Card(2,'m')
except:
    print("Must only use strings 's', 'h', 'c', 'd'")

    

# Test cases where rank and suit are valid
c = card.Card(11,'s')
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())



