# -*- coding: utf-8 -*-
"""
@author: jcrawford
"""

##Problem: Given a roman numeral, convert it to an integer.
##My solution (no google): make a dictionary, iterate through letters of string and add or subtract as needed
class Solution:
    def romanToInt(self, s: str) -> int:
        #dictionary of roman numeral values
        romandict = {    
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100, 
            "D":500,
            "M":1000    
            }
        num = 0
        #iterate through letters in the roman numeral string
        for count, letter in enumerate(s):
            #if it's the last letter in the string, add value
            if count == len(s)-1:
                num = num + romandict[letter]
            #if I comes before X/V, X before L/C, or C comes before D/M, subtract the value of that letter instead of adding
            elif (letter == "I" and s[count+1] in ("X","V")) or (letter == "X" and s[count+1] in ("L","C"))\
            or (letter == "C" and s[count+1] in ("D","M")):
                num = num - romandict[letter]
            else:
                num = num + romandict[letter]
        return num

##Better solution: wasn't far off on this one. solution agrees that using a dictionary and looking at letter individually is the way to go
    #main difference is that this has simplified logic to simply check if the value of a letter is smaller than the one that comes after it 
    #(subtract if so, otherwise add) it then adds the value of the last letter on return statement

class NotMySolution:
    def romanToInt(self, s: str) -> int:
        romandict = {    
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100, 
            "D":500,
            "M":1000    
            }
        num = 0
        for i in range(0, len(s) - 1):
            if romandict[s[i]] < romandict[s[i+1]]:
                num = num - romandict[s[i]]
            else:
                num = num + romandict[s[i]]
        return num + romandict[s[-1]]
print(str(NotMySolution.romanToInt(NotMySolution, "CMIX")))
