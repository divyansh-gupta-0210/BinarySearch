# Univalue Tree
# Given a binary tree root, return whether all values in the tree are the same.

# Constraints

# n ≤ 100,000 where n is the number of nodes in root
# Example 1
# Input
# root = [2, [2, [2, null, null], null], [2, [2, null, null], null]]
# Output
# True
# Explanation
# Every node has the value 2

# Example 2
# Input
# root = [2, [2, [9, null, null], null], [2, null, null]]
# Output
# False
# Explanation
# There is a node with a value 9 while others are 2

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        return self.search(root, root.val)

    def search(self, node, same_data):
        if node is None:
            return True
        if node.val != same_data:
            return False

        return self.search(node.left, same_data) and self.search(node.right, same_data)
