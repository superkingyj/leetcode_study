from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # TC -> O(N)
        # SC -> O(N)
        
        if not root: return []
        
        q = deque([root])
        result = []
        
        while q:
            node_cnt = len(q)
            level = []
            for i in range(node_cnt):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(level)
                
        reverse = False 
        for item in result:
            if reverse: item.reverse()
            reverse = not reverse
        
        return result