def magic(root):
    count = 0 
    def dfs(node):
        nonlocal count
        if node is None:
            return 0 

        if node.left is None and node.right is None:
            return 1 

        left = dfs(node.left)
        right = dfs(node.right)

        if (left!=0 and right != 0) and (left%2) != (right % 2):
            count += 1 
        return left + right + 1
    dfs(root)
    return count 
        