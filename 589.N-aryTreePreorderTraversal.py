"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result