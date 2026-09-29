# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        visited = set()
        def dfs(node):
            if node is None:
                return False 

            target = k - node.val

            if target in visited:
                return True 

            visited.add(node.val)

            left_res = dfs(node.left)

            if left_res:
                return True 

            right_res = dfs(node.right)

            if right_res:
                return True

            return False 

        return dfs(root)