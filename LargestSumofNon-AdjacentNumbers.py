# Largest Sum of Non-Adjacent Numbers
# Given a list of integers nums, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# Constraints

# n ≤ 100,000 where n is the length of nums.
# Example 1
# Input
# nums = [2, 4, 6, 2, 5]
# Output
# 13
# Explanation
# We can take 2, 6, and 5 to get 13.

# Example 2
# Input
# nums = [5, 1, 1, 5]
# Output
# 10
# Explanation
# We can take 5 + 5 since they are not adjacent.

# Example 3
# Input
# nums = [-10, -22, -18, -3, -100]
# Output
# 0
# Explanation
# We don't pick any negative numbers.


class Solution:
    def solve(self, nums):
        including = 0
        excluding = 0
        for i in nums:
            new_excluding = max(including, excluding)
            including = excluding + i
            excluding = new_excluding
        
        return max(including, excluding)
      
      
 
# Intuition
# Loop for all elements in list and maintain two sums Including and Excluding. where Including = Max sum including the previous element, and Excluding= Max sum excluding the previous element.

# Implementation
# First I take, a variable that starts from nums[0] and that is including. And another one is excluding that is 0.
# Including means - Maximum sum including the previous element,
# Excluding means - Maximum sum excluding the previous element.

# Then, I iterate through the array, and find the max. between the two variable.
# In the including part I add the excluding and the current element. and in the excluding part I give a value from the max.
# With this we get the maximum of the number if we include that number, or if we dont Include that number, which we can fit it.
# Similarly it goes on, and in the end we return the maximum of Excluding and Including.

# Time Complexity
# O(n) As we have to iterate through the list to get the maximum sum.

# Space Complexity
# O(n) as we are again and again giving the values to the variables in the list during iteration.
