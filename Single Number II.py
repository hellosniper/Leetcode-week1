# Single Number II.py
# Question: Given an array of integers, every element appears three times except for one. Find that single one.
#           Note:
#           Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#           
# Question from: https://oj.leetcode.com/problems/single-number-ii/
# Sulotion:  using a counter to count bit digit of the number

# Author: DongDing 
# Date: 2014/06/25
# Time complexity:  O(n * 32)
# space complexity:  O(32)  
# Tag: # bitwise, # logic operation
# Comment: following 2 methods is logic operation, too hard for me to understand
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit_count = [0 for i in range(32)]
        for number in A:
            for i in range(32):
                if (number>>i)&1 == 1:
                    bit_count[i] += 1
                    bit_count[i] = bit_count[i] % 3
        result = 0
        if bit_count[31] == 0:
            for i in range(31):
                result |= bit_count[i]<<i
        else: 
            for i in range(31):
                if bit_count[i] == 0:
                    result |= 1<<i
            result = (result +1)*-1
        return result 
    # def singleNumber(self, A):
        # ones = 0
        # twos = 0
        # for i in range(len(A)): 
        #     twos |= ones & A[i];
        #     ones ^= A[i];
        #     threes = ones & twos;
        #     ones &= ~threes;
        #     twos &= ~threes;
        # return ones
        
        #public int singleNumber(int[] A) {
            #int ones = 0, twos = 0;
            #for(int i = 0; i < A.length; i++){
                #ones = (ones ^ A[i]) & ~twos;
                #twos = (twos ^ A[i]) & ~ones;
            #}
            #return ones;
        #}
        
lists = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
lists = [-11,12,14,14,14,12,-11,-11,15,15,15,12,-12355]

a = Solution()
print a.singleNumber(lists)
