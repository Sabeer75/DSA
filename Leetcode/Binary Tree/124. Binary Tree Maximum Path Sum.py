# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        maxi = float('-inf')
        def dfs(node):
            nonlocal maxi 
            node_sum = 0 

            if node is None:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)
            if lh < 0:
                lh = 0
            if rh < 0: 
                rh = 0 
            node_sum = (node.val + lh + rh)
            maxi = max(maxi,node_sum)

            return node.val + max(lh,rh)
        dfs(root)
        return maxi