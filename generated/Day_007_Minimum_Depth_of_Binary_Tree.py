"""
    Day 007
    Title: Minimum Depth of Binary Tree
    Topic: Tree, Breadth-First Search (BFS)
    Difficulty: Easy
    Date: 2026-02-16
    """

# Problem:
# Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth_binary_tree(root: TreeNode) -> int:
    """
    Calculates the minimum depth of a binary tree using Breadth-First Search (BFS).

    The minimum depth is the number of nodes along the shortest path
    from the root node down to the nearest leaf node.
    A leaf is a node with no children.

    Args:
        root: The root node of the binary tree.

    Returns:
        The minimum depth of the tree. Returns 0 if the tree is empty.
    """
    if not root:
        return 0

    # Initialize a queue for BFS, storing tuples of (node, current_depth)
    queue = collections.deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        # If the current node is a leaf, we've found the shortest path to a leaf.
        # Since BFS explores level by level, this is guaranteed to be the minimum depth.
        if not node.left and not node.right:
            return depth

        # Enqueue left child if it exists, with its depth incremented
        if node.left:
            queue.append((node.left, depth + 1))

        # Enqueue right child if it exists, with its depth incremented
        if node.right:
            queue.append((node.right, depth + 1))

    # This line should theoretically not be reached for a valid non-empty tree,
    # as a leaf node will always be found and returned.
    return 0

# Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case, we visit each node exactly once.
    # Space Complexity: O(W), where W is the maximum width of the binary tree. In the worst case (e.g., a complete binary tree), W can be approximately N/2, so the space complexity is O(N) to store nodes in the queue.

