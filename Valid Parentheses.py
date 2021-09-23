# -*- coding: utf-8 -*-
"""
@author: jcrawford
"""

##Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if: Open brackets must be closed by the same type of brackets.Open brackets must be closed in the correct order.

##MySolution: create a dictionary mapping opening to closing symbols, then iterate through the string appending opening symbols to a list and popping
#from the end of that list every time a closing symbol appears, making sure it maps correctly. Assuming no issues, return whether the list is empty
class Solution:
    def isValid(self, s: str) -> bool:
        #creating dictionary relating starting to ending symbols
        symboldict = {
            ")":"(",
            "]":"[",
            "}":"{"
            }
        #list that will hold ([{ in order
        strtsy = []
        for letter in s:
            #if symbol is a starting symbol, append it to the end of the list
            if letter in symboldict.values():
                strtsy.append(letter)
            else:
                #if this isn't a starting symbol and there aren't any starting symbols in strtsy, this is automatically invalid
                if len(strtsy) == 0:
                    return False
                #pop the most recently appended value from startsy and confirm that this symbol lines up with what is being closed
                elif strtsy.pop(len(strtsy)-1) != symboldict[letter]: 
                    return False
        #as one last check, make sure strtsy is now empty, meaning all parentheses, brackets, and braces are closed
        return len(strtsy) == 0
print(Solution.isValid(Solution, "("))

##BetterSolution: Seemingly none! Other recommended answers were essentially this. .pop was the key to making this a straightforward task