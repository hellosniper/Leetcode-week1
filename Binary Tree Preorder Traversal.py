# Binary Tree Preorder Traversal.py
# Question: Given a binary tree, return the pretorder traversal of its nodes' values.
#           For example:Given binary tree {1,#,2,3}, return [1,2,3].

#           
# Question from: https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
# Sulotion: Iteration

# Author: DongDing 
# Date: 2014/06/28
# Time complexity:  O(n)
# space complexity:  
# Tag: linked list   
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
         ##iteration solution 
        if root == None:
            return []
        result = []
        stack1 = []
        stack1.append(root)
        prev = None  # store the node that was visited by the previous step
        while stack1:
            curr = stack1.pop()
            stack1.append(curr)

            if prev == None or curr == prev.left or curr == prev.right: # going down of the tree
                result.append(curr.val)
                if curr.left != None:
                    stack1.append(curr.left)
                elif curr.right != None:
                    stack1.append(curr.right)
                else: 
                    stack1.pop() # leaf 
            elif curr.left == prev: # coming from left
                if curr.right != None: # going to the right
                    stack1.append(curr.right)
                else:
                    
                    stack1.pop() # leaf 
            elif curr.right == prev: # coming from right
                #result.append(curr.val)
                stack1.pop() # leaf   
            prev = curr
        return result
