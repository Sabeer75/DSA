from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root, start):
        if root is None:
            return 0
        parent = {}
        start_node = None
        def parent_check(node):
            nonlocal start_node
            if node is None:
                return 
            
            if node.left:
                parent[node.left] = node 

            if node.right:
                parent[node.right] = node
            if node.val == start:
                start_node = node

            parent_check(node.left)
            parent_check(node.right)

        parent_check(root)

        q = deque([start_node])
        visited = set([start_node])
        distance = 0 

        while q:
            size = len(q)
        
            for _ in range(size):
                node = q.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])

            distance += 1
        return distance-1 if distance !=0 else 0 