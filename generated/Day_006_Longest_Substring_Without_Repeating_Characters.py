"""
    Day 006
    Title: Longest Substring Without Repeating Characters
    Topic: Sliding Window
    Difficulty: Medium
    Date: 2026-02-13
    """

# Problem:
# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

def length_of_longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without duplicate characters.

    This function uses a sliding window approach with a hash set to keep track of
    characters within the current window. The 'right' pointer expands the window,
    and if a duplicate is found, the 'left' pointer shrinks the window until the
    duplicate is removed.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Time Complexity: O(n)
    # Space Complexity: O(min(n, m))

