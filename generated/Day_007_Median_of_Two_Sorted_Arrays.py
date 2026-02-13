"""
    Day 007
    Title: Median of Two Sorted Arrays
    Topic: Arrays, Binary Search, Divide and Conquer
    Difficulty: Hard
    Date: 2026-02-13
    """

# Problem:
# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays. The overall run time complexity
    should be O(log (m+n)).

    This function finds the median by performing a binary search on the partition
    of the shorter array. The goal is to find a partition 'i' in nums1 and 'j'
    in nums2 such that the combined left half of the merged array has the correct
    number of elements and the elements are correctly ordered across the partition.

    Specifically, we aim to satisfy two conditions:
    1. The total number of elements in the left partitions (i + j) equals
       (len(nums1) + len(nums2) + 1) // 2.
    2. The maximum element in the combined left partition is less than or equal
       to the minimum element in the combined right partition.
       This translates to: nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i].

    The binary search adjusts 'i' (the partition point in nums1) to find the
    correct balance. If nums1[i-1] is too large, 'i' needs to decrease. If
    nums2[j-1] is too large, 'i' needs to increase.

    Args:
        nums1 (list[int]): The first sorted array.
        nums2 (list[int]): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.
    """
    # Ensure nums1 is the shorter array to optimize binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    # total_left_half_len is the number of elements in the left partition of the merged array.
    # (m + n + 1) // 2 covers both odd and even total lengths for the left partition size.
    total_left_half_len = (m + n + 1) // 2

    while low <= high:
        # i is the partition point for nums1 (number of elements taken from nums1 for the left half)
        i = (low + high) // 2
        # j is the partition point for nums2
        j = total_left_half_len - i

        # Determine elements at the boundaries of the partitions
        # Use float('-inf') or float('inf') for edge cases where a partition is empty
        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]

        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        # Check if the partition is correct
        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
            # Correct partition found
            # Calculate median
            if (m + n) % 2 == 1:  # Total length is odd
                return float(max(nums1_left_max, nums2_left_max))
            else:  # Total length is even
                return float(max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
        elif nums1_left_max > nums2_right_min:
            # nums1_left_max is too large, meaning we took too many elements from nums1 for the left half.
            # Move the partition point i to the left.
            high = i - 1
        else: # nums2_left_max > nums1_right_min
            # nums2_left_max is too large, meaning we took too few elements from nums1 for the left half.
            # Move the partition point i to the right.
            low = i + 1

    # This line should ideally not be reached if inputs are valid sorted arrays.
    return 0.0 # Or raise an appropriate error if invalid input is possible

# Time Complexity: O(log(min(m, n)))
    # Space Complexity: O(1)

