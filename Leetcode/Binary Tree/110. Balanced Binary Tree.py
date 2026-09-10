# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if node is None:
                return 0 

            count_l = dfs(node.left)
            if count_l == -1:
                return -1
            count_r = dfs(node.right)
            if count_r == -1:
                return -1
            if abs(count_l - count_r)>1:
                return -1
            
            return max(count_l,count_r) + 1

        return dfs(root) != -1 
