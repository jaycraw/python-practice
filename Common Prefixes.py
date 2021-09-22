# -*- coding: utf-8 -*-
"""
@author: jcrawford
"""

##Problem: Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string ""

#My Solution
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        #variable to store the longest common prefix to date. By default, we start with the full length of the 1st word
        longestprefix = strs[0]
        #iterate through all other items in the array after the 1st
        for listnum in range(1,len(strs)):
            charnum = 0
            wordprefix = ""
            #for the given word in the array, compare it to the first word. If it contains the first word, set wordprefix = first word and exit the while loop,
            #otherwise, take off the last letter in the first word and start again
            while charnum <= len(strs[0])-1:
                #have to do this if statement because python doesn't really like [:-0], but I find this ugly and almost certainly improvable
                #does the job tho ¯\_(ツ)_/¯
                if charnum == 0:
                    if  strs[listnum].startswith(strs[0]):
                        wordprefix = strs[0]
                        charnum = len(strs[0]) 
                    else:
                        charnum += 1
                else:
                    if strs[listnum].startswith(strs[0][:-charnum] ):
                        wordprefix =strs[0][:-charnum]
                        charnum = len(strs[0])
                    else: charnum += 1
            #after finding the longest common prefix, see if the preiovus longestprefix is in wordprefix, if not, use the shorterwordprefix
            if longestprefix not in wordprefix:
                longestprefix = wordprefix
        return longestprefix
            
#Better Solution: fairly similar to my solution, but key difference is that it loops letter by letter through the shortest word 
    #and then compares each letter to rather than looping through each word and then comparing those words to the first

    #This version runs quicker and is more compact in terms of lines of code
class NotMySolution: 
    def longestCommonPrefix(self, strs) -> str:
        #is a blank parameter is passed, return empty string
        if not strs:
            return ""
        #find the shortest word. Thought about doing this instead of the first word, but didn't realize there was an easy python function for this
        #that avoids having to loop through the list
        shortest = min(strs,key=len)
        #iterate through letters in the shortest word. If at any point that character does not line up with that number character in the other words, return
        #the string one letter shorter than that
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
    
print(Solution.longestCommonPrefix(Solution,['catch','caterham','dog']))