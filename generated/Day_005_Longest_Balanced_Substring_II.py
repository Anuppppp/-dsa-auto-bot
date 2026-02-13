"""
    Day 005
    Title: Longest Balanced Substring II
    Topic: Hash Map, Prefix Sums, String
    Difficulty: Medium
    Date: 2026-02-13
    """

# Problem:
# Longest Balanced Substring II
# 
# You are given a string s consisting only of the characters 'a', 'b', and 'c'.
# 
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
# 
# Return the length of the longest balanced substring of s.

import collections

def longest_balanced_substring_ii(s: str) -> int:
    """
    Finds the length of the longest balanced substring in a given string s.

    A substring is considered balanced if all distinct characters within it
    appear the same number of times. The string s consists only of 'a', 'b', and 'c'.

    The problem is solved using a prefix sum and hash map approach.
    We iterate through the string, maintaining prefix counts of 'a', 'b', and 'c'.
    For each ending index `j`, we look for a starting index `i` such that the
    substring `s[i...j]` is balanced.

    A substring s[i...j] with counts (C_a, C_b, C_c) is balanced if:
    1. C_a = C_b = C_c = k > 0 (all three characters present)
    2. C_a = C_b = k > 0, C_c = 0 (only 'a' and 'b' present)
    3. C_a = C_c = k > 0, C_b = 0 (only 'a' and 'c' present)
    4. C_b = C_c = k > 0, C_a = 0 (only 'b' and 'c' present)
    5. C_a = k > 0, C_b = 0, C_c = 0 (only 'a' present)
    6. C_b = k > 0, C_a = 0, C_c = 0 (only 'b' present)
    7. C_c = k > 0, C_a = 0, C_b = 0 (only 'c' present)

    For each of these 7 cases, we define a "state" based on differences between
    prefix counts or absolute prefix counts. If two prefix states are identical
    according to a specific case's definition, the substring between their indices
    satisfies the count conditions for that case. We then verify that the
    actual counts are positive for the required characters and zero for others.

    Let `ca[k]`, `cb[k]`, `cc[k]` be the counts of 'a', 'b', 'c' in `s[0...k-1]`.
    For a substring `s[i...j]`, its counts are `C_a = ca[j+1] - ca[i]`, etc.

    The states for the hash maps are defined as follows:
    - Case 1 (k, k, k): `(ca - cb, ca - cc)`
    - Case 2 (k, k, 0): `(ca - cb, cc)`
    - Case 3 (k, 0, k): `(ca - cc, cb)`
    - Case 4 (0, k, k): `(cb - cc, ca)`
    - Case 5 (k, 0, 0): `(cb, cc)`
    - Case 6 (0, k, 0): `(ca, cc)`
    - Case 7 (0, 0, k): `(ca, cb)`

    Each map stores `(state_tuple): first_prefix_end_index`.
    The `first_prefix_end_index` is `i` such that `s[0...i-1]` has that state.
    When we find a current prefix `s[0...j]` with the same state as `s[0...i-1]`,
    the substring `s[i...j]` is a candidate. Its length is `(j+1) - i`.

    Time Complexity: O(N)
    We iterate through the string once to build prefix counts (O(N)).
    Then we iterate through the string again (N+1 times for prefix states).
    For each prefix state, we perform 7 hash map lookups/insertions, which are O(1) on average.
    The number of distinct keys in each hash map is O(N).
    Total time complexity is O(N).

    Space Complexity: O(N)
    `prefix_counts_list` stores N+1 tuples (O(N)).
    Each of the 7 hash maps can store up to N+1 distinct keys (O(N)).
    Total space complexity is O(N).
    """
    n = len(s)
    if n == 0:
        return 0

    max_len = 0

    # prefix_counts_list[k] stores (count_a, count_b, count_c) for s[0...k-1]
    # prefix_counts_list[0] is (0,0,0) for empty prefix
    prefix_counts_list = [(0, 0, 0)] * (n + 1)
    current_ca, current_cb, current_cc = 0, 0, 0

    for k in range(n):
        if s[k] == 'a':
            current_ca += 1
        elif s[k] == 'b':
            current_cb += 1
        else: # s[k] == 'c'
            current_cc += 1
        prefix_counts_list[k+1] = (current_ca, current_cb, current_cc)

    # Initialize maps for each of the 7 cases
    # Each map stores: (key_tuple): first_index_i
    # first_index_i is the length of the prefix that resulted in this key_tuple
    # e.g., map_k_k_k[(0,0)] = 0 means empty prefix (length 0) has (ca-cb=0, ca-cc=0)
    # Using n + 1 as a sentinel value for 'not found'
    maps = {
        "k_k_k": collections.defaultdict(lambda: n + 1), # (ca-cb, ca-cc)
        "k_k_0": collections.defaultdict(lambda: n + 1), # (ca-cb, cc)
        "k_0_k": collections.defaultdict(lambda: n + 1), # (ca-cc, cb)
        "0_k_k": collections.defaultdict(lambda: n + 1), # (cb-cc, ca)
        "k_0_0": collections.defaultdict(lambda: n + 1), # (cb, cc)
        "0_k_0": collections.defaultdict(lambda: n + 1), # (ca, cc)
        "0_0_k": collections.defaultdict(lambda: n + 1)  # (ca, cb)
    }

    # Initialize maps with the state of an empty prefix (index 0)
    maps["k_k_k"][(0, 0)] = 0
    maps["k_k_0"][(0, 0)] = 0
    maps["k_0_k"][(0, 0)] = 0
    maps["0_k_k"][(0, 0)] = 0
    maps["k_0_0"][(0, 0)] = 0
    maps["0_k_0"][(0, 0)] = 0
    maps["0_0_k"][(0, 0)] = 0

    # Iterate through all possible ending positions (j) of a substring
    # idx_j_plus_1 represents the length of the current prefix s[0...j]
    # and also the index in prefix_counts_list
    for idx_j_plus_1 in range(1, n + 1):
        ca, cb, cc = prefix_counts_list[idx_j_plus_1]

        # Case 1: (k, k, k) => C_a - C_b = 0, C_a - C_c = 0
        key_k_k_k = (ca - cb, ca - cc)
        prev_idx = maps["k_k_k"][key_k_k_k]
        if prev_idx <= idx_j_plus_1: # Check if key was seen before
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            # If C_a > 0, then C_b and C_c must also be > 0 due to diffs being 0
            if sub_ca > 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["k_k_k"][key_k_k_k] == n + 1: # Store first occurrence
            maps["k_k_k"][key_k_k_k] = idx_j_plus_1

        # Case 2: (k, k, 0) => C_a - C_b = 0, C_c = 0
        key_k_k_0 = (ca - cb, cc)
        prev_idx = maps["k_k_0"][key_k_k_0]
        if prev_idx <= idx_j_plus_1:
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            sub_cc = cc - prefix_counts_list[prev_idx][2]
            if sub_ca > 0 and sub_cc == 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["k_k_0"][key_k_k_0] == n + 1:
            maps["k_k_0"][key_k_k_0] = idx_j_plus_1

        # Case 3: (k, 0, k) => C_a - C_c = 0, C_b = 0
        key_k_0_k = (ca - cc, cb)
        prev_idx = maps["k_0_k"][key_k_0_k]
        if prev_idx <= idx_j_plus_1:
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            sub_cb = cb - prefix_counts_list[prev_idx][1]
            if sub_ca > 0 and sub_cb == 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["k_0_k"][key_k_0_k] == n + 1:
            maps["k_0_k"][key_k_0_k] = idx_j_plus_1

        # Case 4: (0, k, k) => C_b - C_c = 0, C_a = 0
        key_0_k_k = (cb - cc, ca)
        prev_idx = maps["0_k_k"][key_0_k_k]
        if prev_idx <= idx_j_plus_1:
            sub_cb = cb - prefix_counts_list[prev_idx][1]
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            if sub_cb > 0 and sub_ca == 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["0_k_k"][key_0_k_k] == n + 1:
            maps["0_k_k"][key_0_k_k] = idx_j_plus_1

        # Case 5: (k, 0, 0) => C_b = 0, C_c = 0
        key_k_0_0 = (cb, cc)
        prev_idx = maps["k_0_0"][key_k_0_0]
        if prev_idx <= idx_j_plus_1:
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            sub_cb = cb - prefix_counts_list[prev_idx][1]
            sub_cc = cc - prefix_counts_list[prev_idx][2]
            if sub_ca > 0 and sub_cb == 0 and sub_cc == 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["k_0_0"][key_k_0_0] == n + 1:
            maps["k_0_0"][key_k_0_0] = idx_j_plus_1

        # Case 6: (0, k, 0) => C_a = 0, C_c = 0
        key_0_k_0 = (ca, cc)
        prev_idx = maps["0_k_0"][key_0_k_0]
        if prev_idx <= idx_j_plus_1:
            sub_cb = cb - prefix_counts_list[prev_idx][1]
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            sub_cc = cc - prefix_counts_list[prev_idx][2]
            if sub_cb > 0 and sub_ca == 0 and sub_cc == 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["0_k_0"][key_0_k_0] == n + 1:
            maps["0_k_0"][key_0_k_0] = idx_j_plus_1

        # Case 7: (0, 0, k) => C_a = 0, C_b = 0
        key_0_0_k = (ca, cb)
        prev_idx = maps["0_0_k"][key_0_0_k]
        if prev_idx <= idx_j_plus_1:
            sub_cc = cc - prefix_counts_list[prev_idx][2]
            sub_ca = ca - prefix_counts_list[prev_idx][0]
            sub_cb = cb - prefix_counts_list[prev_idx][1]
            if sub_cc > 0 and sub_ca == 0 and sub_cb == 0:
                max_len = max(max_len, idx_j_plus_1 - prev_idx)
        if maps["0_0_k"][key_0_0_k] == n + 1:
            maps["0_0_k"][key_0_0_k] = idx_j_plus_1

    return max_len

# Time Complexity: O(N)
    # Space Complexity: O(N)

