class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return None

    # Flatten left and right subtrees
    flatten(root.left)
    flatten(root.right)

    # Store the right subtree
    right_subtree = root.right

    # Move the left subtree to the right
    root.right = root.left
    root.left = None

    # Attach the right subtree at the end of the new right subtree
    current = root
    while current.right:
        current = current.right
    current.right = right_subtree

# Example Execution
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

flatten(root)

# Traversal to check the result
while root:
    print(root.val, end=" -> ")
    root = root.right
