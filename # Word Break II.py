# Word Break II.py
# Question: Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
#           Return all such possible sentences.
#           
# Question from: https://oj.leetcode.com/problems/word-break-ii/
# Sulotion:  from back to front build the table

# Author: DongDing 
# Date: 2014/06/25
# Time complexity:  O(n^2)
# space complexity:  O(n^2)  n is the length of input sring
# Tag: # Dynamic programming, # String
# Comment: wordBreak is my solution, wordBreak1 is from the web


class Solution:
# @param s, a string
# @param dict, a set of string
# @return a list of strings
    def wordBreak(self, s, dicts):
        s_len = len(s)
        smatch = [[] for i in range(s_len)]
        # Dynamic programming
        # from back to front build the table
        for index in range(s_len-1, 0-1 , -1):
            start = index
            stop = s_len
            for index1 in range(start,stop):

                if s[start: index1+1] in dicts:
                    
                    if index1 == s_len -1:
                        smatch[start].extend([s[start: index1+1]])
                    elif smatch[index1+1] != []:
                        for existpath in smatch[index1+1]:
                            smatch[start].extend([ s[start:index1+1 ]+ ' ' + existpath ])                
        return smatch[0]
    
    def wordBreak1(self, s, dicts):
        sLength = len(s)
        sMap = [ [] for i in range(sLength)]
        output = [ [] for i in range(sLength)]
        outputFlag = [False for i in range(sLength)]
        for start in range(sLength):
            for stop in range(start,sLength+1):
                if s[start:stop] in dicts:
                    sMap[start].append(stop)
        self.getResult(s,sMap,0,output,outputFlag)
        return output[0]         
    def getResult(self,s,sMap,start,output,outputFlag):
        for stop in sMap[start]:
            newPath = s[start:stop] if start==0 else ' ' + s[start:stop]
            if stop == len(s):
                if not outputFlag[start]:
                    output[start].append(newPath)
            elif outputFlag[stop]:
                for existedPath in output[stop]:
                    output[start].append(newPath+existedPath)
            else:
                self.getResult(s,sMap,stop,output,outputFlag)
                if outputFlag[stop]:
                    for existedPath in output[stop]:
                        output[start].append(newPath+existedPath)
        outputFlag[start] = True #after all 'stop' are iterated, we are sure that the substring started from 'start' is a learned part
    
   
            
a = Solution()
s = "catsanddog"
dicts = ["cat", "cats", "and", "sand", "dog"]
print a.wordBreak(s, dicts)
print a.wordBreak1(s, dicts)
        
        
