# Tree Sum
# Given a binary tree root, return the sum of all values in the tree.

# Constraints

# n ≤ 100,000 where n is the number of nodes in root
# Example 1
# Input
# root = [1, [2, null, null], [3, [5, null, null], null]]
# Output
# 11
# Explanation
# 11 = 1 + 2 + 3 + 5

# Example 2
# Input
# root = [1, [2, [3, null, null], null], null]
# Output
# 6
# Explanation
# 6 = 1 + 2 + 3

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root:
            return root.val + self.solve(root.right) + self.solve(root.left)
        else:
            return 0
