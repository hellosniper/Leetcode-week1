# Copy List with Random Pointer.py
# Question: A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#           Return a deep copy of the list.
#           
# Question from: https://oj.leetcode.com/problems/copy-list-with-random-pointer/
# Sulotion:  # copy a node after the original node  # recover the random pointer  # separate the copied list from the original list

# Author: DongDing 
# Date: 2014/06/30
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag: # linded list, # 
# Comment: 

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def setbeforehead(self,x):
        node = RandomListNode(x)
        node.next = self
        return node
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None: 
            return None
        #dict_random = dict() # list that store the random pointer of each node
        
        # create each node
        temp = head
        #dict_random.update({temp.label: temp})
        # copy a node after the original node
        while temp != None:                     
            tempnew = RandomListNode(temp.label)
            q = temp.next
            temp.next = tempnew 
            tempnew.next = q
            temp = q
			
        # recover the random pointer
        temp = head
        while temp != None:
    	    tempnew = temp.next
    	    q = temp.random
    	    tempnew.random = q.next if q else None
    	    temp = temp.next.next
			
    	# separate them
    	temp = head
    	headnew = head.next
    	tempnew = headnew
    	while temp != None:
    	    q2 = temp.next  # copied node
    	    if temp.next == None:
		        break
          q1 = temp.next.next # next original node
    	    temp.next = q1
            
          if q2 == headnew:
              pass ## head of the new node

    	    else: ## add copied node to it
        		if q2!= tempnew:
        		    tempnew.next = q2
        		    tempnew = tempnew.next
            	  temp = temp.next
        return headnew

    
list1 = [1,2,3,4,5]
node_1 = RandomListNode(100)
for i in list1:
    #print i
    node_1 = node_1.setbeforehead(i)
#node_2 = ListNode(5)
#for i in list2:
    ##print i
    #node_2 = node_2.setbeforehead(i)
node = node_1

while (node!= None):
    #print node.label
    node = node.next
    

a = Solution()
#node_t, node_t2 = a.patition(node_1)

node = node_1
i = 0
while (node!= None):
    print node.label
    node = node.next
    i+=1
print 'Total Number', i
a = Solution()    
print ""    
node_f = a.copyRandomList(node_1)
node_ = node_f
print ""
i = 0
while (node_!= None):
    print node_.label
    node_ = node_.next    
    i+=1
print "Total Number", i
		
		    
