# Binary Tree Preorder Traversal.py
# Question: Given a binary tree, return the postorder traversal of its nodes' values.
#           For example:Given binary tree {1,#,2,3}, return [3,2,1].

#           
# Question from: https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
# Sulotion: Recursion

# Author: DongDing 
# Date: 2014/06/26
# Time complexity:  O(n)
# space complexity:  O(log(n))
# Tag: linked list   
# Comment: 



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

    def postorderTraversal(self, root):
        if root == None:
            return []
        list1 = []
        left = root.left
        list2 = self.postorderTraversal(left)
        #if list2 != []:
            
        list1.extend(list2)
        
        right = root.right
        list3 = self.postorderTraversal(right)
        #if list3 != []:
        list1.extend(list3)
        
        list1.append(root.val)
        return list1
