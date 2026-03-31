"""
    Day 023
    Title: Gas Station
    Topic: Arrays, Greedy Algorithms
    Difficulty: Medium
    Date: 2026-03-31
    """

# Problem:
# Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# 
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """
    Determines the starting gas station index to complete a circular tour.

    Args:
        gas (list[int]): A list where gas[i] is the amount of gas at station i.
        cost (list[int]): A list where cost[i] is the cost to travel from station i to station i+1.

    Returns:
        int: The starting gas station's index if a circuit can be completed,
             otherwise -1. If a solution exists, it is guaranteed to be unique.
    """
    total_gas = sum(gas)
    total_cost = sum(cost)

    # If total gas is less than total cost, it's impossible to complete the circuit.
    if total_gas < total_cost:
        return -1

    # If a solution exists, it is guaranteed to be unique.
    # We can find it by iterating and tracking current tank level.
    current_tank = 0
    start_station = 0
    n = len(gas)

    for i in range(n):
        current_tank += gas[i] - cost[i]

        # If current_tank drops below zero, it means we cannot start from
        # 'start_station' and reach 'i'. So, we reset the tank and try
        # starting from the next station (i + 1).
        if current_tank < 0:
            current_tank = 0
            start_station = i + 1

    return start_station

# Time Complexity: O(N)
    # Space Complexity: O(1)

