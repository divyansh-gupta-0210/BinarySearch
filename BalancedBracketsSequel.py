# Balanced Brackets Sequel
# Given a string s containing round, curly, and square open and closing brackets, return whether the brackets are balanced.

# Constraints

# n ≤ 100,000 where n is the length of s
# Example 1
# Input
# s = "[(])"
# Output
# False

# Example 2
# Input
# s = "([])[]({})"
# Output
# True

class Solution:
    def solve(self, s):
        my_stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                my_stack.append(i)
            elif not len(my_stack) == 0 and my_stack[-1] == "(" and i == ")":
                my_stack.pop(-1)

            elif not len(my_stack) == 0 and my_stack[-1] == "{" and i == "}":
                my_stack.pop(-1)

            elif not len(my_stack) == 0 and my_stack[-1] == "[" and i == "]":
                my_stack.pop(-1)
    
            else:
                my_stack.append(i)

        if len(my_stack) == 0:
            return True
        else:
            return False
