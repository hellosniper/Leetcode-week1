# Single Number.py
# Question: Given an array of integers, every element appears twice except for one. Find that single one.

# Question from: https://oj.leetcode.com/problems/single-number/
# Sulotion:  
# Author: DongDing 
# Date: 2014/07/01
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # bitwise, # logic operation
# Comment: 
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for number in A:
            result ^= number
        return result
