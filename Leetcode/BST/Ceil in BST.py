'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        ceil = -1 
        node = root
        
        while node:
            
            if node.data == x:
                return node.data
                
            elif node.data > x:
                ceil = node.data 
                node = node.left 
                
            else:
                node = node.right 
                
        return ceil
        
        
        