
# QUESTION

# Balanced Brackets
# You're given a string s consisting solely of "(" and ")". Return whether the parentheses are balanced.

# Example 1
# Input
# s = "()"
# Output
# True

# Example 2
# Input
# s = "()()"
# Output
# True

# Example 3
# Input
# s = ")("
# Output
# False

# Example 4
# Input
# s = ""
# Output
# True

# Example 5
# Input
# s = "((()))"
# Output
# True

# Example 6
# Input
# s = "((()"
# Output
# False

class Solution:
    def solve(self, s):
        counter = 0
        for i in s:
            if i == "(":
                counter += 1
            elif i == ")" and counter > 0:
                counter -= 1
            else:
                return False
        return counter == 0
    
