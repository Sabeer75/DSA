'''
My solution - two workaround but still optimal 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        def palindrome(check):
            l = 0 
            r = len(check) - 1
            while l < r:
                if check[l] != check[r]:
                    return False
                l += 1 
                r -= 1 
            else:
                return True

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
            
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)

            if not palindrome(level):
                return False
        else:
            return True
            

'''
# clean code 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        def dfs(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False 
            if left.val != right.val:
                return False 

            return dfs(left.left,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)
