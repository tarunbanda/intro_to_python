"""
This program takes an integer input and spells out the number 
Tarun Banda
Week4 Assignment
SpellingNumbers.py
"""

n2w = {0:"",1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
n2w2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

"""
    spells the number that is entered by user
    range -999,999,999 to 999,999,999
"""
def spell(num):
    if num < 0: 
        num = abs(num)
        return ("negative " + spell(num))
    if num == 0: return "zero"
    if num < 20: return (n2w[num])# If number i less than 20 uses n2w dictionary to get value
    elif num < 100: # if number is between 20 and 100 runs through spell() 
        if divmod(num,10)[1] != 0:
            return (n2w2[divmod(num,10)[0]-2]+" "+spell(divmod(num,10)[1])) 
        else: 
            return n2w2[divmod(num,10)[0]-2]
    elif num <1000: # for numbers less than a 1000 adds string "hundred" and runs through spell()
        if divmod(num,100)[1] != 0:
            return (n2w[divmod(num,100)[0]] +" hundred and " + spell(divmod(num,100)[1])) 
        else: 
            return n2w[divmod(num,100)[0]]+ " hundred"
    elif num < 1000000: #runs through spell() but adds string "thousand"
        if divmod(num,1000)[1] != 0:
            return (spell(divmod(num,1000)[0]) + " thousand " + spell(divmod(num,1000)[1]))
        else:
            return spell(divmod(num,1000)[0]) + " thousand"
    elif num < 1000000000: #runs through spell() and adds string "millions"
        if divmod(num,1000000)[1] != 0:
            return (spell(divmod(num,1000000)[0]) + " million " + spell(divmod(num,1000000)[1]))
        else:
            return spell(divmod(num,1000000)[0]) + " million"
    else:
        print ("Number is out of range") # prints out of range if number is out of range
        
        
        
print ("Enter a number between -999,999,999 and 999,999,999")
num = input("spell:")
print (spell(num))

"""
===============================================================================
# ======OUTPUT==========
 Enter a number between -999,999,999 and 999,999,999
 spell:985343
 nine hundred and eighty five thousand three hundred and forty three


 Enter a number between -999,999,999 and 999,999,999
 spell:-985432983
 negative nine hundred and eighty five million four hundred and thirty two thousand nine hundred and eighty three

 Enter a number between -999,999,999 and 999,999,999
 spell:19
 nineteen
 
 Enter a number between -999,999,999 and 999,999,999
 spell:-43567
 negative forty three thousand five hundred and sixty seven

 Enter a number between -999,999,999 and 999,999,999
 spell:0
 zero

#===============================================================================
"""
