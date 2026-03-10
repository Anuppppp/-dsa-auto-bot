"""
    Day 018
    Title: Number of 1 Bits
    Topic: Bit Manipulation
    Difficulty: Easy
    Date: 2026-03-10
    """

# Problem:
# Number of 1 Bits
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

def hamming_weight(n: int) -> int:
    """
    Calculates the number of set bits (1s) in the binary representation of a given positive integer.

    This function uses Brian Kernighan's algorithm, which efficiently counts set bits.
    The algorithm works by repeatedly flipping the least significant set bit to 0
    and incrementing a counter until the number becomes 0.
    The operation `n & (n - 1)` effectively removes the rightmost set bit from `n`.

    Args:
        n: A positive integer.

    Returns:
        The number of set bits in the binary representation of n.

    Example:
        hamming_weight(11) == 3  (binary 1011 has three 1s)
        hamming_weight(128) == 1 (binary 10000000 has one 1)
    """
    count = 0
    while n > 0:
        n &= (n - 1) # This operation clears the least significant set bit
        count += 1
    return count

# Time Complexity: O(k), where k is the number of set bits in the input integer n. In the worst case, k can be log(n) (e.g., for n = 2^m - 1, all m bits are set). Therefore, the time complexity is O(log n).
    # Space Complexity: O(1), as only a constant amount of extra space is used for the counter variable.

