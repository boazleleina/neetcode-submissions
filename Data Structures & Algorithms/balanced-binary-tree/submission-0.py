# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.balanced = True

        def blc(node):
            if not node:
                return 0
            left = blc(node.left)
            right = blc(node.right)
            if abs(right-left) > 1:
                self.balanced = False
            return 1 + max(left, right)
        
        blc(root)
        return self.balanced