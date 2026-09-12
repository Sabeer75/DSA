from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        q = deque([(root,0)])
        maxi = 0 

        while q:
            size = len(q)
            first = q[0][1]
            for i in range(size):
                node,index = q.popleft()

                index -= first 

                if node.left:
                    q.append((node.left, 2*index+1))
                if node.right:
                    q.append((node.right, 2*index+2))

                if i == size -1:
                    last = index

                maxi = max(maxi,last+1)
        return maxi 