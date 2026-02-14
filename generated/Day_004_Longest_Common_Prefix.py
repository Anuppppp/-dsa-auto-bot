"""
    Day 004
    Title: Longest Common Prefix
    Topic: String Manipulation
    Difficulty: Easy
    Date: 2026-02-14
    """

# Problem:
# Longest Common Prefix
# If there is no common prefix, return an empty string

def longest_common_prefix(strs):
    """
    Finds the longest common prefix string amongst an array of strings.

    If there is no common prefix, returns an empty string.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix string.
    """
    if not strs:
        return ""

    # If there's only one string, it's the common prefix
    if len(strs) == 1:
        return strs[0]

    # Take the first string as a reference for comparison
    first_str = strs[0]

    # Iterate through each character of the first string
    for i in range(len(first_str)):
        char = first_str[i]

        # Compare this character with the character at the same position
        # in all other strings
        for j in range(1, len(strs)):
            # If the current string is shorter than the current index 'i'
            # or if the characters do not match, then the common prefix ends here.
            if i == len(strs[j]) or strs[j][i] != char:
                # Return the common prefix found so far
                return first_str[0:i]

    # If we've iterated through all characters of the first string
    # and found no mismatches, then the first string itself is the LCP.
    return first_str

# Time Complexity: O(N * L_min), where N is the number of strings in the input list, and L_min is the length of the shortest string. In the worst case, we iterate through each character of the shortest string (up to L_min characters), and for each character, we compare it with the corresponding character in all N-1 other strings.
    # Space Complexity: O(1), as we only use a few extra variables for indices and characters. The space for the output string is not counted towards auxiliary space complexity.

