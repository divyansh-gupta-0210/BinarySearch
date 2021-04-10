# Special Product List
# Given a list of integers nums, return a new list such that each element at index i of the new list is the product of all the numbers in the original list except the one at i. Do this without using division.

# Constraints

# 2 ≤ n ≤ 100,000 where n is the length of nums
# Example 1
# Input
# nums = [1, 2, 3, 4, 5]
# Output
# [120, 60, 40, 30, 24]
# Explanation
# 120 = 2 * 3 * 4 * 5, 60 = 1 * 3 * 4 * 5, and so on.

# Example 2
# Input
# nums = [3, 2, 1]
# Output
# [2, 3, 6]

class Solution:
    def solve(self, nums):
        
        answer = [1] * len(nums)
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        
        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i-1]
        
        for i in range(len(nums) - 1, 0, -1):
            backward[i-1] = backward[i] * nums[i]
        
        for i in range(0, len(nums)):
            answer[i] = forward[i] * backward[i]
        
        return answer
