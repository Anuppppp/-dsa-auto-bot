"""
    Day 022
    Title: Text Justification
    Topic: Arrays, Strings, Greedy Algorithms
    Difficulty: Medium
    Date: 2026-03-30
    """

# Problem:
# Text Justification
# 
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
# 
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

def text_justification(words: list[str], max_width: int) -> list[str]:
    """
    Formats a given text (list of words) into lines, where each line has exactly
    max_width characters and is fully (left and right) justified, except for the
    last line which is left-justified.

    The approach is greedy:
    1. Words are packed into a line as long as they fit within max_width,
       considering at least one space between words.
    2. Once a line is full, it is justified:
       a. Calculate the total number of spaces needed to fill max_width.
       b. If there's only one word on the line, it's left-justified with
          trailing spaces.
       c. If there are multiple words, spaces are distributed as evenly as
          possible among the gaps between words. Extra spaces (if total spaces
          don't divide evenly by number of gaps) are assigned to gaps from left
          to right.
    3. The last line of text is always left-justified, with a single space
       between words and trailing spaces to fill max_width.

    Args:
        words: A list of strings, where each string is a word.
        max_width: An integer representing the maximum width for each line.

    Returns:
        A list of strings, where each string is a fully justified line.
    """
    result = []
    current_line_words = []
    current_line_length = 0  # Sum of lengths of words in current_line_words

    for word in words:
        # Check if adding the current word to the line would exceed max_width.
        # If current_line_words is empty, no spaces are needed before the first word.
        # Otherwise, at least one space is needed before the new word.

        # Calculate potential length if 'word' is added:
        # current_line_length (sum of word lengths) + len(word) (new word's length)
        # + (1 if current_line_words else 0) (for the space before the new word)

        if not current_line_words:
            # First word on the line
            current_line_words.append(word)
            current_line_length += len(word)
        else:
            # Check if adding 'word' with at least one space fits
            potential_length_with_space = current_line_length + len(word) + 1
            if potential_length_with_space <= max_width:
                current_line_words.append(word)
                current_line_length += len(word)
            else:
                # Current word doesn't fit, justify the previous line
                num_words_in_line = len(current_line_words)
                line = ""

                if num_words_in_line == 1:
                    # Single word line: left-justified with trailing spaces
                    line = current_line_words[0] + " " * (max_width - current_line_length)
                else:
                    # Multiple words: distribute spaces evenly
                    total_spaces_to_distribute = max_width - current_line_length
                    num_gaps = num_words_in_line - 1

                    base_spaces_per_gap = total_spaces_to_distribute // num_gaps
                    extra_spaces_for_left_gaps = total_spaces_to_distribute % num_gaps

                    for i in range(num_gaps):
                        line += current_line_words[i]
                        spaces_to_add = base_spaces_per_gap
                        if i < extra_spaces_for_left_gaps:
                            spaces_to_add += 1
                        line += " " * spaces_to_add
                    line += current_line_words[num_words_in_line - 1] # Add the last word

                result.append(line)

                # Start a new line with the current word
                current_line_words = [word]
                current_line_length = len(word)

    # After the loop, handle the last line (if any words are left)
    if current_line_words:
        # Last line is always left-justified with single spaces between words
        last_line = " ".join(current_line_words)
        last_line += " " * (max_width - len(last_line))
        result.append(last_line)

    return result

# Time Complexity: O(N * maxWidth), where N is the number of words and maxWidth is the maximum line width. In the worst case, each word might form its own line, and constructing each line takes O(maxWidth) time due to string concatenation. More precisely, it's O(sum(len(line) for line in result)), which is O(num_lines * maxWidth).
    # Space Complexity: O(N * maxWidth), primarily for storing the `result` list. In the worst case, all words could be on separate lines, each of `maxWidth` length. `current_line_words` can store up to N words, but its total character length is bounded by `maxWidth`.

