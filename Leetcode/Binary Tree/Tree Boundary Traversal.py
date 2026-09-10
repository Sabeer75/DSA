'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        
        res = []
        res.append(root.data)
        
        if root.left is None and root.right is None:
            return res 
            
        def left_boundary(node):
            while node:
                if node.left or node.right:
                    res.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right 
                
        def leaf(node):
            if node is None:
                return 
            
            if node.left is None and node.right is None:
                res.append(node.data)
                return 
                
            leaf(node.left)
            leaf(node.right)
            
        def right_boundary(node):
            omit = []
            while node:
                if node.right or node.left:
                    omit.append(node.data)
                    
                if node.right:
                    node = node.right 
                else:
                    node = node.left 
                    
            res.extend(omit[::-1])
            
        left_boundary(root.left)
        leaf(root)
        right_boundary(root.right)
        
        return res 
                
                
                
            