# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _dfs(self, node, idx, depth):
        self.visited.add(idx)

        if depth >= self.deepest_leaves_depth: 
            if depth == self.deepest_leaves_depth:
                self.deepest_leaves_sum += node.val
            else:
                self.deepest_leaves_sum = node.val
                self.deepest_leaves_depth = depth
        
        if node.left and idx+1 not in self.visited:
            self._dfs(node.left, idx+1, depth+1)
            self.visited.remove(idx+1)
            
        if node.right and idx+2 not in self.visited:
            self._dfs(node.right, idx+2, depth+1)
            self.visited.remove(idx+2)
        
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.visited = set()
        self.deepest_leaves_sum = 0
        self.deepest_leaves_depth = 0
        self._dfs(root, 0, 0)
        return self.deepest_leaves_sum
        
        