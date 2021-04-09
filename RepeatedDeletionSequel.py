# Repeated Deletion Sequel
# Given a string s and an integer k, repeatedly delete the earliest k consecutive duplicate characters.

# Constraints

# k, n ≤ 100,000 where n is the length of s.
# Example 1
# Input
# s = "baaabbdddd"
# k = 3
# Output
# "d"

# Explanation
# First we delete the "a"s to get "bbbdddd". Then we delete the "b"s to get "dddd". Then we delete three of the four "d"s to get "d"

class Solution:
    def solve(self, s, k):
        while True:
            c = 0
            ch = set(s)
            for i in ch:
                if i * k in s:
                    s = s.replace(i * k, "")
                    c += 1
            if count == 0:
                break
        return s
