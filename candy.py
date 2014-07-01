# candy.py
# Children with a higher rating get more candies than their neighbors.
# Question: There are N children standing in a line. Each child is assigned a rating value.
#           You are giving candies to these children subjected to the following requirements:
#                    Each child must have at least one candy.
#                    Children with a higher rating get more candies than their neighbors.
#           What is the minimum candies you must give?
#           
# Question from: https://oj.leetcode.com/problems/candy/
# Sulotion:  iteratively read the relation between the ajacent ratings: < = >

# Author: DongDing 
# Date: 2014/07/01
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # linear list # extreme points
# Comment: 
import sys
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        #  
        length = len(ratings)
        if length == 0:
            return 0
        # initialization for ratings[0]
        sum_candy =1 
        backup = 1
        current = 1
        peak = 9223372036854775807  # sys.maxint
        #
        for i in range(1, length, 1 ):
            if ratings[i] > ratings[i-1]:
                peak += 1
                current += 1
                sum_candy += current
                #backup = 0
            
            elif  ratings[i] == ratings[i-1]:
                ## 
                current = 1
                sum_candy += current
                peak = 9223372036854775807 # sys.maxint
                backup = 1
                
            else: # <
                if current != 1:  # come from > 
                    peak = current
                    current = 1
                    backup = 1
                    sum_candy += current
                else: # come from == or <
                    backup += 1
                    sum_candy += backup
                    
                    if backup == peak:            
                        sum_candy += 1
                        peak +=1
                    
        return sum_candy
        # 
ratings = [1,2,3,3,5,1]
ratings = [1,0,2]
ratings = [2,1]
a= Solution()
print a.candy(ratings)
