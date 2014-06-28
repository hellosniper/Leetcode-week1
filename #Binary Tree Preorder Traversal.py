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
# Comment: iteration solution  and recurtion sulution



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
                if curr.left != None:
                    stack1.append(curr.left)
                elif curr.right != None:
                    stack1.append(curr.right)
                else: 
                    result.append(curr.val)
                    stack1.pop() # leaf 
            elif curr.left == prev: # coming from left
                if curr.right != None: # going to the right
                    stack1.append(curr.right)
                else:
                    result.append(curr.val)
                    stack1.pop() # leaf 
            elif curr.right == prev: # coming from right
                result.append(curr.val)
                stack1.pop() # leaf   
            prev = curr
        return result
        
    # def postorderTraversal(self, root):
          ## recursion solution
    #     if root == None:
    #         return []
    #     list1 = []
    #     left = root.left
    #     list2 = self.postorderTraversal(left)
    #     #if list2 != []:
            
    #     list1.extend(list2)
        
    #     right = root.right
    #     list3 = self.postorderTraversal(right)
    #     #if list3 != []:
    #     list1.extend(list3)
        
    #     list1.append(root.val)
    #     return list1
