def hasPathSum(root, targetSum):
    if not root:
        return False
    
    # Check if it's a leaf node
    if not root.left and not root.right:
        return targetSum == root.val

    # Recursively check left and right subtrees
    targetSum -= root.val
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

# Example Execution
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

target_sum_example = 22
print("Path Sum Result:", hasPathSum(root, target_sum_example))
