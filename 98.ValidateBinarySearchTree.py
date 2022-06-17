from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, left, right):
        print(left, None if not root else root.val, right)
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.dfs(root, -2**31-1, 2**31)

ex1 = [5,4,6,None,None,3,7]
node_1 = TreeNode()
node_1.val = ex1[0]
node_1.left = TreeNode()
node_1.left.val = ex1[1]
node_1.right = TreeNode()
node_1.right.val = ex1[2]
node_1.left.left = ex1[3]
node_1.left.right = ex1[4]
node_1.right.left = TreeNode()
node_1.right.right = TreeNode()
node_1.right.left.val = ex1[5]
node_1.right.right.val = ex1[6]

sol = Solution()
print(sol.isValidBST(node_1))
