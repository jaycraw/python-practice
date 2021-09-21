# -*- coding: utf-8 -*-
"""
@author: jcrawford
"""
### My original solution
class Solution:
    #Must provide array with only 1 valid answer
    def twoSum(self, nums, target):
        n = 0
        #iterate though entire array for first number being summed
        while n < len(nums):
            m = n + 1
            #only iterate through items later in the array than n 
            while m < len(nums):
                #if our chosen items in the array add to achieve our target, return indices and celebrate accordingly
                if nums[n] + nums[m] == target:
                    return [n,m]
                m = m + 1
            n = n + 1

### more elegant solution I learned.
    #Enumerate(x) returns two variables, both count and value
### by using a dict and doing target - value 1, only need to go through the list once
class notMySolution:
    def twoSumBetter(self,nums,target):
        numdict = {}
        for count, val in enumerate(nums):
            secval = target - val
            if secval in numdict:
                return [numdict[secval],count]
            else: numdict[val] = count

x = notMySolution.twoSumBetter(notMySolution,[1000,-600,50,12],-588)
#format output prettily
print("[" + str(x[0]) + "], [" + str(x[1]) + "]")

