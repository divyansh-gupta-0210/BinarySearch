# Length of Longest Balanced Subsequence
# Given a string s containing brackets "(" and ")", return the length of the longest subsequence of balanced brackets.

# Constraints

# n ≤ 100,000 where n is length of s.
# Example 1
# Input
# s = "())(()"
# Output
# 4
# Explanation
# We can take the subsequence "()()"

# Example 2
# Input
# s = "))(("
# Output
# 0
# Explanation
# We can't take any letters from s that's balanced, so the longest balanced subsequence is "" (empty string).

# Example 3
# Input
# s = "))()))()"
# Output
# 4
# Explanation
# We can take the subsequence "()()". Note that characters in the subsequence do not have to be contiguous.

# Example 4
# Input
# s = "((((())"
# Output
# 4
# Explanation
# We can make the subsequence (()).

class Solution:
    def solve(self, s):
        stack = []
        c = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")" and len(stack) == 0:
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                c += 2
                stack.pop()
            else:
                stack.append(i)

        return c
