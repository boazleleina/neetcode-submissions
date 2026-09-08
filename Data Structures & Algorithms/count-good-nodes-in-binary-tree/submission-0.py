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
        

        def good(node, maxSoFar):
            if not node:
                return 0
            count = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            count += good(node.left, maxSoFar)
            count += good(node.right, maxSoFar)
            return count
        return good(root, root.val)
           