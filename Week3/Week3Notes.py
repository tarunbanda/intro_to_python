'''phoneBook = {'mickey': '213-333-2341', 'minnie': '510-540-2390', 'goofy': '818-399-2763'}


for a in sorted(phoneBook):
    print (a + ' has phone number ' + phoneBook[a])'''
    
    
""" generates a random number between 1 and 10, and asks the user to guess what it is
"""

import random  # needed to use randint()
secretNumber = random.randint(1,10)

userGuess = int(input("Pick a number between 1 and 10: "))

while userGuess != secretNumber:
    if userGuess > secretNumber:
        userGuess = int(input("Your guess is too high, please try again: "))
    elif userGuess < secretNumber:
         userGuess = int(input("Your guess is too low, please try again: "))
    else:
        break
    
print ("Correct! The secret number was: " + str(secretNumber)) 
    
'''else:
     print ("Wrong, the number is " + str(secretNumber))'''

    