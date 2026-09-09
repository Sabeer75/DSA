''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        res= []
        curr = root 
        
        while curr:
            
            if curr.left is None:
                res.append(curr.data)
                curr = curr.right 
                
            else:
                predes = curr.left
                
                while predes.right and predes.right != curr:
                    predes = predes.right 
                    
                if predes.right is None:
                    predes.right = curr 
                    
                    curr = curr.left 
                    
                else:
                    predes.right = None 
                    res.append(curr.data)
                    curr = curr.right
                    
        return res 
                    