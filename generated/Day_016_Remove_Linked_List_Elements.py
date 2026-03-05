"""
    Day 016
    Title: Remove Linked List Elements
    Topic: Linked List
    Difficulty: Easy
    Date: 2026-03-05
    """

# Problem:
# Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_linked_list_elements(head: ListNode, val: int) -> ListNode:
    """
    Removes all nodes from a linked list that have Node.val == val.

    Args:
        head: The head of the linked list.
        val: The integer value to remove.

    Returns:
        The new head of the linked list after removal.
    """
    # Create a dummy node that points to the head of the original list.
    # This simplifies handling cases where the head itself needs to be removed.
    dummy = ListNode(0)
    dummy.next = head

    current = dummy

    # Iterate through the list using 'current' as the node *before* the one we are checking.
    # This allows us to easily modify 'current.next' to skip nodes.
    while current.next:
        if current.next.val == val:
            # If the next node's value matches 'val', skip it.
            # This effectively removes current.next from the list.
            current.next = current.next.next
        else:
            # If the next node's value does not match 'val', move to the next node.
            current = current.next

    # The new head of the list is dummy.next
    return dummy.next

# Time Complexity: O(N), where N is the number of nodes in the linked list. We traverse the list once.
    # Space Complexity: O(1), as we only use a few extra pointers (dummy, current) regardless of the list size.

