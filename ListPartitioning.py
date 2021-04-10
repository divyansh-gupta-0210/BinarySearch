# List Partitioning
# Given a list of strings strs, containing the strings "red", "green" and "blue", partition the list so that the red come before green, which come before blue.

# This should be done in \mathcal{O}(n)O(n) time.

# Bonus: Can you do it in \mathcal{O}(1)O(1) space? That is, can you do it by only rearranging the list (i.e. without creating any new strings)?

# Constraints

# n ≤ 100,000 where n is the length of strs.
# Example 1
# Input
# strs = ["green", "blue", "red", "red"]
# Output
# ["red", "red", "green", "blue"]

class Solution:
    def solve(self, strs):
        left = 0
        right = len(strs)-1
        current = 0
        while current<=right:
            if strs[current] == "red":
                strs[left], strs[current] = strs[current],strs[left]
                left += 1
                current +=1
            elif strs[current] == "blue":
                strs[right], strs[current] = strs[current],strs[right]
                right -= 1
            else:
                current += 1
                
        return strs
