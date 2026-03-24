"""
    Day 019
    Title: Container With Most Water
    Topic: Arrays, Two Pointers
    Difficulty: Medium
    Date: 2026-03-24
    """

# Problem:
# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

def container_with_most_water(height: list[int]) -> int:
    """
    Finds two lines that together with the x-axis form a container,
    such that the container contains the most water.

    Args:
        height: An integer array where height[i] is the height of the i-th line.

    Returns:
        The maximum amount of water a container can store.
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the width of the current container
        current_width = right - left

        # The height of the container is limited by the shorter of the two lines
        current_height = min(height[left], height[right])

        # Calculate the area of the current container
        current_area = current_width * current_height

        # Update the maximum water found so far
        max_water = max(max_water, current_area)

        # Move the pointer pointing to the shorter line inward
        # This is because moving the shorter line might allow us to find a taller line,
        # potentially increasing the effective height and thus the area.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Time Complexity: O(n)
    # Space Complexity: O(1)

