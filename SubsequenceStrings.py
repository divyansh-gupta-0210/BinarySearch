# Given two lowercase alphabet strings s1 and s2, determine if s1 is a subsequence of s2.

# Constraints

# n ≤ 100,000 where n is the length of s1
# m ≤ 100,000 where m is the length of s2

# Example 1
# Input
# s1 = "ppl"
# s2 = "apple"
# Output
# True

# Example 2
# Input
# s1 = "ale"
# s2 = "apple"
# Output
# True

# Example 3
# Input
# s1 = "elppa"
# s2 = "apple"
# Output
# False

class Solution:
    def solve(self, s1, s2):
        a = len(s1)
        b = len(s2)
        i = 0
        j = 0

        while i < a and j < b:
            if s1[i] == s2[j]:
                i += 1
            j += 1

        return i == a
