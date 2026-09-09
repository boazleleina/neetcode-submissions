class Solution:
    def buildTree(self, preorder, inorder):
        # Build the hashmap ONCE: value -> its index in inorder.
        # This lets us find any node's split-point in O(1) instead of scanning.
        idx = {val: i for i, val in enumerate(inorder)}

        # A single pointer that walks through preorder left-to-right.
        # We use a list so the nested function can mutate it (or use self.pre_idx).
        self.pre_idx = 0

        def build(left, right):
            # left, right = the window into INORDER that this subtree occupies.
            # If the window is empty, there's no subtree here.
            if left > right:
                return None

            # The next preorder element is this subtree's root.
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1                  # consume it, advance the pointer
            node = TreeNode(root_val)

            # Find where this root sits in inorder -> splits left vs right.
            mid = idx[root_val]

            # LEFT FIRST: preorder emits the whole left subtree before the right,
            # so the pointer must consume left-subtree nodes before reaching the right root.
            node.left = build(left, mid - 1)   # inorder positions before the root
            node.right = build(mid + 1, right) # inorder positions after the root

            return node

        # Kick off on the full inorder array: positions 0 .. len-1.
        return build(0, len(inorder) - 1)