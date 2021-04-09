# Given a string s, repeatedly delete the earliest consecutive duplicate characters.

# Constraints

# n ≤ 100,000 where n is the length of s.
# Example 1
# Input
# s = "abbbaac"
# Output
# "c"
# Explanation
# "bbb" are the earliest consecutive duplicate characters which gets deleted. So we have "aaac".
# "aaa" then gets deleted to end up with "c".

class Solution:
    def solve(self, st):
        l = [""]
        s = ""
        for i in st:
            if i == l[-1]:
                l.pop()
            elif s == i:
                pass
            else:
                l.append(i)
            s = i

        return "".join(l)
