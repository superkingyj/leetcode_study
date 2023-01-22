from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def traverse(p):
            if p == None: return
            
            traverse(p.left)
            result.append(p.val)
            traverse(p.right)
        
        traverse(root)
        return result    