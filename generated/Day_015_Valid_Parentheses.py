"""
    Day 015
    Title: Valid Parentheses
    Topic: Stack
    Difficulty: Easy
    Date: 2026-03-04
    """

# Problem:
# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def is_valid_parentheses(s: str) -> bool:
    """
    Determines if the input string 's' contains valid parentheses.

    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    Args:
        s (str): The input string containing only '(', ')', '{', '}', '[' and ']'.

    Returns:
        bool: True if the input string is valid, False otherwise.
    """
    stack = []
    # A map to quickly check the corresponding opening bracket for each closing bracket
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in bracket_map.values():  # It's an opening bracket
            stack.append(char)
        elif char in bracket_map:  # It's a closing bracket
            # If stack is empty, no opening bracket to match, or if the top of stack
            # doesn't match the expected opening bracket for the current closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
        # For any other character (though problem statement implies only brackets), it would be ignored

    # After iterating through all characters, if the stack is empty,
    # all opening brackets have been correctly closed.
    return not stack

# Time Complexity: O(n)
    # Space Complexity: O(n)

