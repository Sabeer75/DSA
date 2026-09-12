# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None 

        root_value = preorder[0]
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left = len(left_inorder)

        left_preorder = preorder[1:left+1]
        right_preorder = preorder[left+1:]

        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)

        return root 