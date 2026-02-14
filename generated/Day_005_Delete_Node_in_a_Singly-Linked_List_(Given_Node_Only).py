"""
    Day 005
    Title: Delete Node in a Singly-Linked List (Given Node Only)
    Topic: Linked List
    Difficulty: Medium
    Date: 2026-02-14
    """

# Problem:
# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.\
# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.

def delete_node(node) -> None:
    """
    Deletes a given node from a singly-linked list.

    This function takes a node from a singly-linked list and deletes it.
    Crucially, it does not have access to the head of the list.
    It is guaranteed that the given node is NOT the last node in the list.
    All values in the list are unique.

    The deletion is achieved by overwriting the value of the given node
    with the value of its successor node. Then, the given node's 'next'
    pointer is updated to point to its successor's successor, effectively
    removing the successor node from the list. This makes the given node
    take on the identity of its successor, and the original value of the
    given node is no longer present in the list. The total number of nodes
    decreases by one.

    Args:
        node: The node to be deleted. It is guaranteed to have a 'next' node.
              Assumes a ListNode class exists with 'val' and 'next' attributes.
              Example: class ListNode:
                           def __init__(self, x):
                               self.val = x
                               self.next = None

    Returns:
        None. The operation modifies the linked list in-place.
    """
    # Copy the value of the next node into the current node.
    # This effectively replaces the current node's value with its successor's value.
    node.val = node.next.val

    # Bypass the next node.
    # Make the current node's 'next' pointer point to the node after the next node.
    # This removes the original next node from the list.
    node.next = node.next.next

# Time Complexity: O(1)
    # Space Complexity: O(1)

