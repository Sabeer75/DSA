'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        floor = -1 
        
        node = root 
        
        while node:
            if node.data == k:
                return k 
            elif node.data < k:
                floor = node.data
                node = node.right 
                
            else:
                node = node.left 
                
        return floor