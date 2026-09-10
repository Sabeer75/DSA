class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    pre = []
    ino = []
    post = []

    s = []
    s.append([root,1])

    while (len(s)>0):
        p = s[-1]

        if p[1] == 1:
            s[-1][1] += 1 

            pre.append(p[0].val)
            if p[0].left:
                s.append([p[0].left,1])

        elif p[1] == 2:
            s[-1][1] += 1

            ino.append(p[0].val)
            if p[0].right:
                s.append([p[0].right,1])

        else:
            post.append(p[0].val)

            del s[-1]

    return f"{pre}\n{ino}\n{post}"

# Create the tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Run inorder traversal
print(inorder(root))