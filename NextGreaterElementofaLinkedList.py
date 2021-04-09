# Given a singly linked list node, replace every node's value with the first greater node's value to its right. If a node doesn't have a next greater node, set its value to 0.

# Constraints

# n ≤ 100,000 where n is the number of nodes in node
# Example 1
# Input
# node = [3, 2, 4, 5]
# Output
# [4, 4, 5, 0]

# Example 2
# Input
# node = [1, 1, 1, 1]
# Output
# [0, 0, 0, 0]

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        s = []
        a = node
        while node:
            while s and node.val > s[-1].val:
                t = s.pop()
                t.val = node.val
            s.append(node)
            node = node.next
        
        for i in s:
            i.val = 0
        
        return a
