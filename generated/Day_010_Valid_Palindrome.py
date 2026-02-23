"""
    Day 010
    Title: Valid Palindrome
    Topic: Strings
    Difficulty: Easy
    Date: 2026-02-23
    """

# Problem:
# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome after converting all uppercase letters
    into lowercase letters and removing all non-alphanumeric characters.

    A phrase is a palindrome if it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Example:
        is_palindrome("A man, a plan, a canal: Panama") == True
        is_palindrome("race a car") == False
        is_palindrome(" ") == True
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer past non-alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1

        # If alphanumeric characters are found and pointers haven't crossed
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True

# Time Complexity: O(N), where N is the length of the input string. In the worst case, both pointers traverse the entire string once.
    # Space Complexity: O(1), as we only use a few variables for pointers and do not create any new data structures proportional to the input size.

