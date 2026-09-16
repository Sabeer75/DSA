# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        def bst(node,low,high):
            if node is None:
                return True 

            if node.val <= low or node.val >= high:
                return False

            if not bst(node.left,low,node.val):
                return False
            if not bst(node.right,node.val,high):
                return False 
            
            return True
        return bst(root,float('-inf'),float('inf'))