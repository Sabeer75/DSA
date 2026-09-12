"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def paths(self, root):
        # code here
        if root is None:
            return []
                
        res = []
        ds = []
        def dfs(node):
            if node is None:
                return 
            
            ds.append(node.data)

            if node.left is None and node.right is None:
                res.append(ds.copy())
                ds.pop()
                return
            
            dfs(node.left)
            dfs(node.right)
            ds.pop()
            
        dfs(root)
        
        return res 