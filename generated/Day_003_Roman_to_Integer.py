"""
    Day 003
    Title: Roman to Integer
    Topic: String Manipulation, Hash Map
    Difficulty: Easy
    Date: 2026-02-13
    """

# Problem:
# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to its integer equivalent.

    Roman numerals are represented by seven different symbols:
    I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000.

    The function iterates through the Roman numeral string, comparing the value
    of the current symbol with the next. If the current symbol's value is less
    than the next symbol's value (e.g., 'IV' where I < V), it indicates a
    subtractive case, and the current symbol's value is subtracted from the total.
    Otherwise, it's an additive case, and the value is added.

    Args:
        s (str): The Roman numeral string (e.g., "MCMXCIV").

    Returns:
        int: The integer representation of the Roman numeral.

    Examples:
        >>> roman_to_int("III")
        3
        >>> roman_to_int("LVIII")
        58
        >>> roman_to_int("MCMXCIV")
        1994
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        # If not the last character and current symbol's value is less than the next symbol's value
        if i + 1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]

    return total

# Time Complexity: O(N), where N is the length of the Roman numeral string. The algorithm iterates through the string once.
    # Space Complexity: O(1), as the space used for the `roman_map` dictionary is constant and does not depend on the input string length (it always stores 7 key-value pairs).

