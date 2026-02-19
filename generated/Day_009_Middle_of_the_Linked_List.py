"""
    Day 009
    Title: Middle of the Linked List
    Topic: Linked List
    Difficulty: Easy
    Date: 2026-02-19
    """

# Problem:
# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: ListNode) -> ListNode:
    """
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

    Args:
        head (ListNode): The head of the singly linked list.

    Returns:
        ListNode: The middle node of the linked list.
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

# Time Complexity: O(N)
    # Space Complexity: O(1)

