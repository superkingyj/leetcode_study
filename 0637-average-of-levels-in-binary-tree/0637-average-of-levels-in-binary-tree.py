# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _bfs(self, root):
        q = []
        q.append(root)

        while q:
            curr_level_cnt = len(q)
            curr_level_sum = 0
            next_nodes = []

            for node in q:
                curr_level_sum += node.val
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)
            
            self.result.append(curr_level_sum/curr_level_cnt)
            q = next_nodes

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.result = []
        self._bfs(root)
        return self.result
        