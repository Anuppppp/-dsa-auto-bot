"""
    Day 001
    Title: Two Sum
    Topic: Arrays, Hash Tables
    Difficulty: Easy
    Date: 2026-02-13
    """

# Problem:
# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.

    Args:
        nums (list[int]): A list of integers.
        target (int): The target sum.

    Returns:
        list[int]: A list containing the indices of the two numbers that sum up to the target.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return [] # Should not be reached based on problem constraints (exactly one solution)

# Time Complexity: O(n)
    # Space Complexity: O(n)

