# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_val = 0
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.convertBST(root.right)
        self.sum_val += root.val
        root.val = self.sum_val
        self.convertBST(root.left)
        
        return root
        