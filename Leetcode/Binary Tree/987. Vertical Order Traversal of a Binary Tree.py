from collections import deque 
from collections import defaultdict 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        if root is None:
            return []
        q = deque([(root,0,0)])
        res = []
        columns = defaultdict(list)

        while q:
            node , x, y = q.popleft()

            columns[y].append((x,node.val))

            if node.left:
                q.append((node.left,x+1,y-1))
            if node.right:
                q.append((node.right,x+1,y+1))

        for i in sorted(columns):
            columns[i].sort()

            res.append([value for j,value in columns[i]])

        return res 