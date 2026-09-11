from collections import defaultdict, deque
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if root is None:
            return []
        
        q = deque([(root,0,0)])
        res = []
        columns = defaultdict(list)
        
        while q:
            node,x,y = q.popleft()
        
            columns[y].append((x,node.data))
        
            if node.left:
                q.append((node.left,x+1,y-1))
            if node.right:
                q.append((node.right,x+1,y+1)) 
        
        for x in sorted(columns):
            res.append(columns[x][-1][-1])
        
        return res 