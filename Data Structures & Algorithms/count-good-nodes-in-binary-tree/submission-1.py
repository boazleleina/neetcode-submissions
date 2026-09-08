# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def good(node, maxFar):
            if not node:
                return 0
            count = 1 if node.val >= maxFar else 0
            maxFar = max(maxFar, node.val)
            count += good(node.left, maxFar)
            count += good(node.right, maxFar)
            return count
        return good(root, root.val)