# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.best_max = float("-inf")

        def path(node):
            if not node:
                return 0
            
            left = path(node.left)
            right = path(node.right)

            node_sum = node.val + max(0, left) + max(0, right)

            self.best_max = max(self.best_max, node_sum)

            return node.val + max(max(0, left), max(0, right))
        
        path(root)
        return self.best_max