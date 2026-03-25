"""
    Day 020
    Title: Word Pattern
    Topic: Hash Map
    Difficulty: Easy
    Date: 2026-03-25
    """

# Problem:
# Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

def word_pattern(pattern: str, s: str) -> bool:
    """
    Checks if a given string 's' follows the same pattern as 'pattern'.

    This function determines if there is a bijection (one-to-one and onto mapping)
    between letters in the 'pattern' and non-empty words in the string 's'.
    A full match implies that each letter in 'pattern' maps to exactly one unique
    word in 's', and each unique word in 's' maps to exactly one letter in 'pattern'.

    Args:
        pattern (str): The pattern string consisting of lowercase English letters.
        s (str): The input string consisting of lowercase English letters and spaces.

    Returns:
        bool: True if 's' follows the same pattern, False otherwise.

    The approach uses two hash maps to maintain the bijection:
    1. `char_to_word`: Maps characters from 'pattern' to words from 's'.
    2. `word_to_char`: Maps words from 's' to characters from 'pattern'.

    The algorithm proceeds as follows:
    1. Split the input string 's' into a list of words using `s.split()`. This handles
       multiple spaces gracefully by splitting on any whitespace and removing empty strings.
    2. If the number of characters in 'pattern' does not match the number of words,
       a bijection is impossible, so return False.
    3. Iterate through the 'pattern' and 'words' simultaneously using an index.
    4. For each character-word pair:
       a. Check the `char_to_word` map:
          - If the character is already in the map, ensure its mapped word is
            the current word. If not, return False.
          - If the character is not in the map, add the mapping.
       b. Check the `word_to_char` map:
          - If the word is already in the map, ensure its mapped character is
            the current character. If not, return False.
          - If the word is not in the map, add the mapping.
    5. If the loop completes without returning False, it means a valid bijection
       exists, so return True.
    """
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]

        # Check char -> word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        # Check word -> char mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True

# Time Complexity: O(L + N), where L is the total length of the string 's' (due to splitting and iterating through words) and N is the length of the 'pattern'. In the worst case, L dominates N, so it can be simplified to O(L). Hash map operations (insertion, lookup) take O(1) on average.
    # Space Complexity: O(N * K), where N is the length of the 'pattern' (and number of words) and K is the average length of a word. This space is used to store the 'words' list and the two hash maps (`char_to_word` and `word_to_char`), which store up to N distinct words as keys or values. In the worst case, this can be O(L) if all words are distinct and long.

