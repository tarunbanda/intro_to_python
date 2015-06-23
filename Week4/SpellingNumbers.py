"""
This program takes an integer input and spells out the number 
Tarun Banda
Week4 Assignment
SpellingNumbers.py
"""

n2w = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
n2w2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

"""
    spells the number that is entered by user
    range -999,999,999 to 999,999,999
"""
def spell(num):
    if num == 0:
        return ""
    if num < 20: # If number i less than 20 uses n2w dictionary to get value
        return (n2w[num])
    elif num < 100: # if number is between 20 and 100 runs through spell() 
        div = divmod(num,10)
        return (n2w2[div[0]-2]+" "+spell(div[1]))
    elif num <1000: # for numbers less than a 1000 adds string "hundred" and runs through spell()
        div = divmod(num,100)
        if div[1] == 0:
            string = " hundred"
        else:
            string =" hundred and "
        return(n2w[div[0]]+string+spell(div[1]))
    elif num < 1000000: #runs through spell() but adds string "thousand"
        div = divmod(num,1000)
        string = (spell(div[0]) + " thousand ")
        return (string + spell(div[1]))
    elif num < 1000000000: #runs through spell() and adds string "millions"
        div = divmod(num, 1000000)
        string = (spell(div[0]) + " million ")
        return (string + spell(div[1]))
    else:
        print ("Number is out of range") # prints out of range if number is out of range
        
        
print ("Enter a number between -999,999,999 and 999,999,999")
rawnumber = input("spell:")
num = abs(rawnumber) #assigns abs of rawnumber
    
if rawnumber >= 0: #if raw number is positive print answer
    print (spell(num))
else: # if raw number is negative print "negative" 
    print ("negative " + spell(num))