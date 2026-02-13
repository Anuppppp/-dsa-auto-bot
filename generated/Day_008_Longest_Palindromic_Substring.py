"""
    Day 008
    Title: Longest Palindromic Substring
    Topic: String Manipulation, Dynamic Programming, Two Pointers
    Difficulty: Medium
    Date: 2026-02-13
    """

# Problem:
# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

def longest_palindromic_substring(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.

    This problem can be solved using the "Expand Around Center" approach.
    A palindrome can be centered at a single character (for odd-length palindromes like "aba")
    or between two characters (for even-length palindromes like "abba").

    The algorithm iterates through each character in the string, treating it as a potential
    center for an odd-length palindrome. It also considers the space between each character
    and its next character as a potential center for an even-length palindrome.

    For each potential center, it expands outwards, checking if characters on both sides are equal.
    It continues expanding as long as the characters match and the indices are within the string bounds.
    The length of the palindrome found is then compared with the longest palindrome found so far,
    and the start and end indices are updated accordingly.

    Finally, the substring corresponding to the longest palindrome's start and end indices is returned.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring in s.
    """
    if not s or len(s) < 1:
        return s

    start = 0
    end = 0

    def expand_around_center(s_local: str, left: int, right: int) -> int:
        """
        Helper function to expand around a given center (or pair of centers)
        and return the length of the palindrome found.
        """
        while left >= 0 and right < len(s_local) and s_local[left] == s_local[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome

    for i in range(len(s)):
        # Palindrome with odd length (center is s[i])
        len1 = expand_around_center(s, i, i)
        # Palindrome with even length (center is between s[i] and s[i+1])
        len2 = expand_around_center(s, i, i + 1)

        current_max_len = max(len1, len2)

        if current_max_len > (end - start + 1):
            # Update start and end indices based on the current_max_len.
            # For an odd-length palindrome, 'i' is the exact center.
            # For an even-length palindrome, 'i' and 'i+1' are the two center characters.
            # The formula below correctly calculates the start and end for both cases.
            start = i - (current_max_len - 1) // 2
            end = i + current_max_len // 2

    return s[start : end + 1]

# Time Complexity: O(N^2)
    # Space Complexity: O(1)

