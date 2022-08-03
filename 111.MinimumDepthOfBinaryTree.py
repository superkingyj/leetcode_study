from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append((root, 1))
        while True:
            p, d = q.popleft()
            
            if p:
                if not p.left and not p.right:
                    return d
                else:
                    q.append((p.left, d+1))
                    q.append((p.right, d+1))