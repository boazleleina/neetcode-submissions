# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.best_depth = 0

        def dpth(node):
            if not node:
                return 0
            left = dpth(node.left)
            right = dpth(node.right)
            self.best_depth = max(self.best_depth, left+right)
            return 1 + max(left, right)
        
        dpth(root)
        return self.best_depth