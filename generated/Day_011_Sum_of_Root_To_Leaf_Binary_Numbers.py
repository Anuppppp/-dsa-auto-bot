"""
    Day 011
    Title: Sum of Root To Leaf Binary Numbers
    Topic: Binary Tree, Depth-First Search, Bit Manipulation
    Difficulty: Medium
    Date: 2026-02-24
    """

# Problem:
# Sum of Root To Leaf Binary Numbers
# You are given the root of a binary tree where each node has a value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
# The test cases are generated so that the answer fits in a 32-bits integer.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_root_to_leaf_binary_numbers(root: TreeNode) -> int:
    """
    Calculates the sum of all binary numbers represented by root-to-leaf paths in a binary tree.

    Each node in the tree has a value of 0 or 1. A root-to-leaf path forms a binary number,
    where the root is the most significant bit. The function traverses the tree using
    Depth-First Search (DFS), accumulating the binary value along each path. When a leaf
    node is reached, the accumulated binary value is added to a total sum.

    Args:
        root: The root of the binary tree.

    Returns:
        The total sum of all binary numbers represented by root-to-leaf paths.
    """
    total_sum = 0

    def dfs(node, current_val):
        nonlocal total_sum
        if not node:
            return

        # Update the current binary value by shifting left (multiplying by 2)
        # and adding the current node's value. This is equivalent to:
        # current_val = current_val * 2 + node.val
        current_val = (current_val << 1) | node.val

        # If it's a leaf node, add the current_val to total_sum
        if not node.left and not node.right:
            total_sum += current_val
            return

        # Recurse for left and right children
        dfs(node.left, current_val)
        dfs(node.right, current_val)

    dfs(root, 0)
    return total_sum

# Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once during the Depth-First Search traversal.
    # Space Complexity: O(H), where H is the height of the binary tree. This space is used by the recursion stack during the DFS traversal. In the worst case (a skewed tree), H can be N, leading to O(N) space. In the best case (a balanced tree), H is log N, leading to O(log N) space.

