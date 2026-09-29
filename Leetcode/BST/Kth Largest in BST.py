'''Structure of a Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthLargest(self, root, k):
        # code here
        count = 0 
        
        def dfs(node):
            nonlocal count 
            if node is None:
                return None
                
            res = dfs(node.right)
            
            if res is not None:
                return res 
                
            count += 1 
            
            if count == k:
                return node.data
                
            return dfs(node.left)
            
        return dfs(root)