'''
Assignment 2
Name: Tarun Banda
This program is meant to automate printing form letters for upcoming election. 
The form letters should be able to change three fields (addressee, candidate, sender)
'''

letterInfo1 = ('Hildegard', 'Barbara Boxer', 'Brunhilda')
letterInfo2 = ('Cheech','Jerry Brown', 'Chong')
letterInfo3 = ('Tarun','Barack Obama', 'Jerry')

##Store the fields into a list and create the pre-worded letter
letterList = [letterInfo1, letterInfo2, letterInfo3]

letterText = ('Dear %s,\n\nI would like you to vote for %s \n' +
             'because I think he is best for this state \n\n' +
             'Sincerely, \n%s')
##Print the letters with the proper inputs
for x in letterList:
    print (letterText % x)
    print ('\n')
