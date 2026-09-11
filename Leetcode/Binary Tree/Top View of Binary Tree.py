from collections import defaultdict, deque

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
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
            res.append(columns[x][0][1])
            
        return res 