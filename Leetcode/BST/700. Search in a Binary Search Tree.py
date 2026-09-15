# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root,val):
        
        def bst(node):
            if node is None:
                return 

            if node.val == val:
                return node
            elif node.val > val:
                return bst(node.left)
            else:
                return bst(node.right)

        return bst(root) 