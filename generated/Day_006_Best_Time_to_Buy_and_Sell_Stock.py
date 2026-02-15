"""
    Day 006
    Title: Best Time to Buy and Sell Stock
    Topic: Arrays, Greedy
    Difficulty: Easy
    Date: 2026-02-15
    """

# Problem:
# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profit(prices):
    """
    Calculates the maximum profit that can be achieved by buying and selling a stock.

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing
    a different day in the future to sell that stock.

    Args:
        prices (list[int]): An array of stock prices, where prices[i] is the price on day i.

    Returns:
        int: The maximum profit that can be achieved. If no profit can be achieved, returns 0.
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate potential profit if selling at current price
        # and update max_profit if it's higher
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Time Complexity: O(n)
    # Space Complexity: O(1)

