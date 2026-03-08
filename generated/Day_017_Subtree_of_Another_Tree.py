"""
    Day 017
    Title: Subtree of Another Tree
    Topic: Tree, Depth-First Search, Binary Tree
    Difficulty: Easy
    Date: 2026-03-08
    """

# Problem:
# Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    Checks if subRoot is a subtree of root.

    A subtree of a binary tree tree is a tree that consists of a node in tree
    and all of this node's descendants. The tree tree could also be considered
    as a subtree of itself.

    Args:
        root: The root of the main binary tree.
        subRoot: The root of the potential subtree.

    Returns:
        True if subRoot is a subtree of root, False otherwise.
    """
    # Base case: If subRoot is None, it's always a subtree (an empty tree is a subtree of any tree).
    if subRoot is None:
        return True

    # Base case: If root is None but subRoot is not None, then subRoot cannot be a subtree.
    if root is None:
        return False

    # Helper function to check if two trees are identical
    def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, they are identical
        if p is None and q is None:
            return True
        # If one node is None and the other is not, or their values differ, they are not identical
        if p is None or q is None or p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

    # Check if the current 'root' tree is identical to 'subRoot'
    if is_same_tree(root, subRoot):
        return True

    # If not, recursively check if 'subRoot' is a subtree of the left child or the right child
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

# Time Complexity: Let N be the number of nodes in the 'root' tree and M be the number of nodes in the 'subRoot' tree.

The `is_subtree` function traverses each node in the 'root' tree. For each node, it potentially calls `is_same_tree`.

The `is_same_tree` function, in the worst case, visits all M nodes of `subRoot`.

Since `is_subtree` makes a call to `is_same_tree` for each of the N nodes in the `root` tree, the total time complexity is O(N * M).
    # Space Complexity: The space complexity is determined by the maximum depth of the recursion stack.

In the worst case, the `is_subtree` function can have a recursion depth equal to the height of the 'root' tree, which can be O(N) for a skewed tree.

Each call to `is_subtree` then calls `is_same_tree`, which can have a recursion depth equal to the height of the 'subRoot' tree, which can be O(M) for a skewed tree.

Therefore, the total space complexity is O(N + M), which simplifies to O(N) in the typical case where N >= M.

