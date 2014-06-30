# Word Break.py 
# Question: Given a string s and a dictionary of words dict,
#           determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#           
# Question from: https://oj.leetcode.com/problems/word-break/
# Sulotion:  

# Author: DongDing 
# Date: 2014/06/30
# Time complexity:  O(n^2)
# space complexity:  O(n^2)  n is the length of input sring
# Tag: # Dynamic programming, # String
# Comment: wordBreak is my solution, wordBreak1 is from the web


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dicts):
        if s == None:
            return True
        s_len = len(s)
        s_map = [[] for start in range(s_len)] # word  in dicts for s[start] 
        pathexist = [True for start in range(s_len)]
        #start = 0
        for start in range(s_len):
            for stop in range(start,s_len+1):
                if s[start:stop] in dicts:
                    s_map[start].append(stop)
        return self.findPath(s_map,0,s_len,pathexist)
    def findPath(self, s_map, start, stop, pathexist):
        # find if there is a path in s_map from start to stop
        # @param s_map, 
        # @param sart, stop , 
        # building a map pathexist
        # @return a boolean        
        if pathexist[start] == False:
            return False
        for start1 in s_map[start]:
            if start1 == stop:
                return True
            else:
                if self.findPath(s_map, start1, stop, pathexist):
                    return True
        pathexist[start] = False
        return False            
a = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dicts = ["c","aaaaaa","aa","aaaa","b"]
print a.wordBreak(s, dicts)
