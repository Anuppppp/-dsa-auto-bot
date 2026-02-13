"""
    Day 004
    Title: Add Two Numbers
    Topic: Linked Lists
    Difficulty: Medium
    Date: 2026-02-13
    """

# Problem:
# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented by linked lists.

    The digits are stored in reverse order, and each of their nodes contains a single digit.
    This function adds the two numbers and returns the sum as a linked list.

    Args:
        l1: The first non-empty linked list representing a non-negative integer.
        l2: The second non-empty linked list representing a non-negative integer.

    Returns:
        A new linked list representing the sum of the two input numbers.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        current_sum = val1 + val2 + carry
        carry = current_sum // 10
        digit = current_sum % 10

        current.next = ListNode(digit)
        current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return dummy_head.next

# Time Complexity: O(max(N, M)) where N and M are the lengths of the two input linked lists. We iterate through both lists once.
    # Space Complexity: O(max(N, M)) for the new linked list storing the sum. In the worst case, the sum list can have max(N, M) + 1 nodes.
