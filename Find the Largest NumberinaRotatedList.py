# Find the Largest Number in a Rotated List
# You are given a list of unique integers nums that is sorted in ascending order and is rotated at some pivot point. Find the maximum number in the rotated list.

# Can you solve it in \mathcal{O}(\log{}n)O(logn)?

# Constraints

# n ≤ 100,000 where n is the length of nums.
# Example 1
# Input
# arr = [6, 7, 8, 1, 4]
# Output
# 8
# Explanation
# The original sorted array of [1, 4, 6, 7, 8] was rotated at index 2 and results in the input array [6, 7, 8, 1, 4,]. And the largest number is 8.

# Example 2
# Input
# arr = [1, 2, 3]
# Output
# 3

# Example 3
# Input
# arr = [1]
# Output
# 1

# Example 4
# Input
# arr = [10, 1, 2, 3, 4, 7]
# Output
# 10


class Solution:
    def solve(self, arr):
        lo, hi = 0, len(arr)
        left, right = arr[0], arr[-1]

        while lo < hi:
            mid = (lo + hi) // 2
            if left > arr[mid]:
                hi = mid
            else:
                lo = mid + 1

        return arr[lo - 1]
