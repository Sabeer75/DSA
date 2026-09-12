'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        def dfs(node):
            if node is None:
                return True

            if node.left is None and node.right is None:
                return True
            
            if node.left is None:
                if node.right.data != node.data:
                    return False 
                    
            if node.right is None:
                if node.left.data != node.data:
                    return False 
                
            if node.left and node.right:
                if node.left.data + node.right.data != node.data:
                    return False
                    
            if not dfs(node.left):
                return False 
            if not dfs(node.right):
                return False 
            return True 
            
        return dfs(root)