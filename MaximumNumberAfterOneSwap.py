# Given an integer n, you can swap any two digits at most once. Return the maximum value of the resulting number.

# Constraints

# 0 ≤ n < 2 ** 31
# Example 1
# Input
# n = 1929
# Output
# 9921
# Explanation
# We swap the first and the last digits

class Solution:
    def solve(self, n):
        s = list(str(n))
        max_ = n
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if s[j] > s[i]:
                    s[i], s[j] = s[j], s[i]
                    max_ = max(max_, int("".join(s)))
                    s[i], s[j] = s[j], s[i]
        return max_
