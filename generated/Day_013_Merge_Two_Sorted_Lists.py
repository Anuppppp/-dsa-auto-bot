"""
    Day 013
    Title: Merge Two Sorted Lists
    Topic: Linked Lists
    Difficulty: Easy
    Date: 2026-02-26
    """

# Problem:
# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into one sorted list.

    The list should be made by splicing together the nodes of the first two lists.

    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    # Create a dummy node to simplify the merging process
    dummy = ListNode()
    current = dummy

    # Iterate while both lists have nodes
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If one list is exhausted, append the remaining nodes of the other list
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    # The merged list starts from dummy.next
    return dummy.next

# Time Complexity: O(m + n)
    # Space Complexity: O(1)

