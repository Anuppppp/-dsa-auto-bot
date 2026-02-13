"""
    Day 002
    Title: Palindrome Number
    Topic: Mathematics
    Difficulty: Easy
    Date: 2026-02-13
    """

# Problem:
# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome_number(x: int) -> bool:
    """
    Checks if an integer is a palindrome without converting it to a string.

    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x: The integer to check.

    Returns:
        True if x is a palindrome, False otherwise.
    """
    # Handle edge cases:
    # 1. Negative numbers are not palindromes (e.g., -121 is not 121-).
    # 2. Numbers ending in 0 (except 0 itself) are not palindromes.
    #    For example, 120 cannot be a palindrome because its reverse would be 021.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    # Build the reverted_number until it's greater than or equal to x.
    # This effectively reverses the second half of the number.
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        x //= 10

    # When the loop terminates, we have two cases:
    # 1. The original number had an even number of digits:
    #    x and reverted_number should be equal (e.g., x=12, reverted_number=12 for 1221).
    # 2. The original number had an odd number of digits:
    #    x will be equal to reverted_number // 10 (e.g., x=1, reverted_number=12 for 121).
    #    The middle digit of an odd-length palindrome doesn't affect its palindromic property,
    #    so we can discard it from reverted_number by integer division.
    return x == reverted_number or x == reverted_number // 10

# Time Complexity: O(log N), where N is the input integer. The number of digits in N is approximately log10(N). In each step of the while loop, we effectively remove one digit from 'x', thus the number of iterations is proportional to the number of digits in N.
    # Space Complexity: O(1), as we only use a few constant extra variables to store 'reverted_number' and perform comparisons, regardless of the input integer's size.

