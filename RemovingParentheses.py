# Given a string of parentheses s, return the minimum number of parentheses to be removed to make the string balanced.

# Constraints

# n ≤ 100,000 where n is the length of s
# Example 1
# Input
# s = "()())()"
# Output
# 1
# Explanation
# We can remove the ")" at index 4 to make it balanced.

# Example 2
# Input
# s = ")("
# Output
# 2
# Explanation
# We must remove all the parentheses.


class Solution:
    def solve(self, s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")" and len(stack) == 0:
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)

        return len(stack)
