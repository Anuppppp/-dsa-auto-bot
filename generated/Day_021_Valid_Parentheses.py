"""
    Day 021
    Title: Valid Parentheses
    Topic: Stack
    Difficulty: Easy
    Date: 2026-03-27
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
    Determines if the input string of parentheses is valid.

    A string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    The approach uses a stack to keep track of open brackets. When an open bracket
    is encountered, it's pushed onto the stack. When a close bracket is encountered,
    the top of the stack is checked. If the stack is empty or the top element
    doesn't match the corresponding open bracket, the string is invalid.
    After processing all characters, if the stack is empty, the string is valid.

    Args:
        s (str): The input string containing just '(', ')', '{', '}', '[' and ']'.

    Returns:
        bool: True if the input string is valid, False otherwise.
    """
    stack = []
    # Map closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in bracket_map.values():  # It's an opening bracket
            stack.append(char)
        elif char in bracket_map:  # It's a closing bracket
            # If stack is empty, no corresponding open bracket found
            # Or if the top of the stack doesn't match the expected open bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
        # For any other character not specified in the problem, it would be ignored
        # or considered invalid depending on stricter requirements. Here, we assume
        # only valid bracket characters are in 's'.

    # If the stack is empty, all open brackets were correctly closed
    return not stack

# Time Complexity: O(n), where 'n' is the length of the input string. We iterate through the string once, and each stack operation (push, pop, peek) takes O(1) time.
    # Space Complexity: O(n), where 'n' is the length of the input string. In the worst-case scenario (e.g., a string like "((((("), the stack could store all 'n' opening brackets.

