# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return None

        root_value = postorder[-1]
        root = TreeNode(root_value)
        root_index = inorder.index(root_value)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left = len(left_inorder)

        left_postorder = postorder[0:left]
        right_postorder = postorder[left:-1]

        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)

        return root 