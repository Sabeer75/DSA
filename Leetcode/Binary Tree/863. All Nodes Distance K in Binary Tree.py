from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root,target, k):
        parent = {}
        def find_parent(node):
            if node is None:
                return 
            
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node

            find_parent(node.left)
            find_parent(node.right)

        find_parent(root)

        q = deque([target])
        visited = set([target])
        distance = 0 

        while q:
            size = len(q)
            if distance == k:
                return [node.val for node in q]

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
        return []
                    
