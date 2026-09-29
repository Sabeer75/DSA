class Solution:
    def kthSmallest(self, root, k):
        count = 0 

        def dfs(node):
            nonlocal count

            if node is None:
                return None 

            res = dfs(node.left)

            if res is not None:
                return res 
            
            count += 1 

            if count == k:
                return node.val
            
            return dfs(node.right)

        return dfs(root)