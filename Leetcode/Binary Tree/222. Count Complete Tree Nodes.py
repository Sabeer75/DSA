"""
So basically if the lh == rh return the (2**lh) - 1 
but if the lh != rh go a step ahead in both side and find the height again which is 1 + node.left + node.right
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):

        if root is None:
            return 0 

        lh = 0 
        rh = 0 

        left = root 
        right = root

        while left:
            lh += 1 
            left = left.left 

        while right:
            rh += 1 
            right = right.right 

        if lh == rh: 
            return (2**lh) -1 
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            