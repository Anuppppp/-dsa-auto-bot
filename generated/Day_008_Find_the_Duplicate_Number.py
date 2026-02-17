"""
    Day 008
    Title: Find the Duplicate Number
    Topic: Arrays, Cycle Detection (Floyd's Tortoise and Hare)
    Difficulty: Medium
    Date: 2026-02-17
    """

# Problem:
# Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.

def find_duplicate(nums: list[int]) -> int:
    """
    Finds the duplicate number in an array using Floyd's Tortoise and Hare algorithm.

    Given an array of integers nums containing n + 1 integers where each integer is
    in the range [1, n] inclusive. There is only one repeated number in nums,
    and it must be returned.

    The solution must not modify the array nums and must use only constant extra space.

    The problem can be modeled as finding the cycle entry point in a linked list.
    Imagine each index `i` points to `nums[i]`. Since all numbers are in the range
    [1, n], and there are n+1 numbers, a duplicate must exist. This duplicate
    creates a cycle in the sequence of pointers. The index 0 is outside the cycle
    because nums[i] >= 1 for all i.

    Steps:
    1. Initialize two pointers, `slow` and `fast`. `slow` starts at `nums[0]`,
       `fast` starts at `nums[nums[0]]`. This is because index 0 is the start
       of the path leading to the cycle, and we want to enter the "value space"
       where the cycle exists.
    2. Move `slow` one step (`slow = nums[slow]`) and `fast` two steps
       (`fast = nums[nums[fast]]`) until they meet. This meeting point is
       guaranteed to be within the cycle.
    3. Once they meet, reset `slow` to `0` (the conceptual head of the list
       before entering the cycle). Keep `fast` at the meeting point.
    4. Move both `slow` and `fast` one step at a time (`slow = nums[slow]`,
       `fast = nums[fast]`) until they meet again. This second meeting point
       is the entry point of the cycle, which is the duplicate number.
    """
    slow = nums[0]
    fast = nums[nums[0]]

    # Phase 1: Find the intersection point of the two pointers
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # Phase 2: Find the entrance to the cycle
    # Reset slow to the start (index 0)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Time Complexity: O(N)
    # Space Complexity: O(1)

