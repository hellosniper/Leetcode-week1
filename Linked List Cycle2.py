# Linked List Cycle2.py
# Question: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#           Follow up: Can you solve it without using extra space?
#           
# Question from: https://oj.leetcode.com/problems/linked-list-cycle-ii/
# Sulotion: # let fast runner to catch up with the slow runner, then slow back to head ,then meet again

# Author: DongDing 
# Date: 2014/06/25
# Time complexity:  O(n)
# space complexity:  O(0)
# Tag: linked list   
# Comment: 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        
        if head == None or head.next == None:
            return None
        if head.next.next == head:
            return head
        fast = head.next.next
        slow = head.next
        while fast != slow:
            if fast == None:
                return None
            else:
                fast = fast.next
                slow = slow.next
            if fast == None:
                return None
            else:
                fast = fast.next

        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
        
        
        
        
        
