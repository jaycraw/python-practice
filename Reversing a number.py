# -*- coding: utf-8 -*-
"""
@author: jcrawford
"""

##Problem:
    #Given a signed 32-bit integer x, return x with its digits reversed. 
    #If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    #Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    
##My Solution (no googling):
class Solution:
    def reverse(self, x: int) -> int:
        #iterate through the string appending each letter to an array
        digitlist = []
        negativesign = False
        #if there is a negative sign, turn bit to true, otherwise, append as usual
        for count, letter in enumerate(str(x)):
            if letter == "-":
                negativesign = True
            else:
                digitlist.append(letter)
        #iterate through the array in reverse order, reconstructing a number string, 
            #starting with a negative sign if necessary
        if negativesign:
            finalNumString = "-"
        else:
            finalNumString = ""
        n = len(digitlist) - 1
        #don't append anything until a nonzero number is found
        nonzero = False
        while n >= 0:
            if digitlist[n] != str(0) or nonzero:
                nonzero = True
                finalNumString = finalNumString + digitlist[n]
            n = n - 1
        #check to make sure this is a signed 32 bit integer
        try:
            if int(finalNumString) > (2**31)-1:
                finalNumString = 0
        except ValueError:
            finalNumString = 0
        try:
            if int(finalNumString) < (-2)**31:
                finalNumString = 0
        except ValueError:
            finalNumString = 0        
        #return final result
        return finalNumString

##The better solution (after researching other options)
    #I definitely forgot that (::-1) exists, so I had to recreate a ton of the logic that is done for you by
    #simply converting the absolute value of x into a string, reversing it, converting back into an int
    #and then applying original negative sign if necessary

class NotMySolution:
    def reverse(self, x: int) -> int:
        #returns 1 or -1, convert to int or sign is a float, messing the later string up
        sign = int(x/abs(x))
        #make x positive, cast it as a string, reverse it, and cast it back to an int
        flippedunsigned = int(str(x*sign)[::-1])
        #apply your sign, but return 0 if the unsigned number is bigger than 2^31
        return sign * flippedunsigned * (flippedunsigned < 2**31)

print(str(NotMySolution.reverse(NotMySolution, -561)))
