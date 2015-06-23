'''
*** Assignment 2
*** Name: Tarun Banda 
*** This program takes in a series of inputs (addressee, candidate, and sender
*** and automates inserting their information into a pre-worded letter. 
'''

## Instruction on how to enter data
print ("Enter addressee followed by, candidate, and sender.\n" +
       "Hit return after entering each field.\n" +
       "Hit return twice to print letters")

## Creating a loop that adds inputs to a list 
def letterFields():
    try:
        while True: 
            fields = raw_input("Enter fields one at a time: ")
            if not fields: break
            yield fields
    except KeyboardInterrupt:
        return

##Store the fields into a list and create the pre worded letter
letterInfo = list(letterFields())
tempList = []
letterText = ('Dear %s,\n\nI would like you to vote for %s \n' +
             'because I think he is best for this state \n\n' +
             'Sincerely, \n%s')
##Print the letters with the proper inputs
for n in range(1,len(letterInfo)):
    if n % 3 == 0:
        tempList = letterInfo[n-3:n]
        convertToTuple = tuple(tempList)
        print (letterText % convertToTuple)
        print ('\n')
        
