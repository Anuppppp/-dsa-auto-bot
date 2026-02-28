"""
    Day 014
    Title: Invert Binary Tree
    Topic: Tree, Recursion
    Difficulty: Easy
    Date: 2026-02-28
    """

# Problem:
# Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root: TreeNode) -> TreeNode:
    """
    Inverts a binary tree by swapping the left and right children of each node recursively.

    Args:
        root: The root node of the binary tree.

    Returns:
        The root node of the inverted binary tree.
    """
    if not root:
        return None

    # Swap the left and right children of the current node
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

# Time Complexity: O(N)
    # Space Complexity: O(H)

