# Given a list of integers nums, find the first missing positive integer. In other words, find the lowest positive integer that does not exist in the list. The list can contain duplicates and negative numbers as well.

# Constraints

# n ≤ 100,000 where n is the length of nums.
# Example 1
# Input
# nums = [1, 2, 3]
# Output
# 4

# Example 2
# Input
# nums = [3, 4, -1, 1]
# Output
# 2

# Example 3
# Input
# nums = [1, 2, 0]
# Output
# 3

# Example 4
# Input
# nums = [-1, -2, -3]
# Output
# 1

class Solution:
    def solve(self, nums):
        n = set(nums)
        i = 1
        while True:
            if i not in n:
                return i
            i += 1
