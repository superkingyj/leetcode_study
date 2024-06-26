# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def _bfs(self):
        q = deque()
        q.append(self.root)
        result = []
        
        while q:
            max_val = -float('inf')
            l = len(q)
            
            for i in range(l):
                node = q.popleft()
                if node: 
                    max_val = max(max_val, node.val)
                    if node.left: 
                        q.append(node.left)
                    if node.right: 
                        q.append(node.right)
        
            result.append(max_val)
            
        return result
                
        
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.root = root
        return self._bfs()