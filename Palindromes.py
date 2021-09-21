# -*- coding: utf-8 -*-
"""
@author: jcrawford
"""

##Problem: Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert x to a string and check if the string is equal to itself reversed
        return (str(x) == str(x)[::-1])
    
chk = Solution.isPalindrome(Solution, 1001)
print(chk)

#Better solution: for once, I actually got the best answer! \o/ Clean one line solution, albeit this is mostly because
#Python has a built in string reversal. If this function didn't exist, my first thought would be to use some array looping
#to break up the string into it's constituent letters and reconstruct a reversed string by looping through the array from back
#to front test