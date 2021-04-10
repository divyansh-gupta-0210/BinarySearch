# 0-1 Knapsack
# You are given two lists of integers weights and values which have the same length and an integer capacity. weights[i] and values[i] represent the weight and value of the ith item.

# Given that you can take at most capacity weights, and that you can only take at most one copy of each item, return the maximum amount of value you can get.

# Constraints

# n ≤ 250 where n is the length of weights and values
# capacity ≤ 250
# Example 1
# Input
# weights = [1, 2, 3]
# values = [1, 5, 3]
# capacity = 5
# Output
# 8

class Solution:
    def solve(self, weights, values, capacity):
        n = len(weights)
        t = [[0 for j in range(capacity + 1)] for i in range(n+1)]
        for i in range(n + 1):
            for j in range(capacity + 1):
                if i == 0 or j == 0:
                    t[i][j] = 0
                elif weights[i-1] <= j:
                    t[i][j] = max(t[i-1][j-weights[i-1]] + values[i-1], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][capacity]
