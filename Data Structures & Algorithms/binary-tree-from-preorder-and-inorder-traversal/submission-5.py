class Solution:
    def buildTree(self, preorder, inorder):
        #check the base case
        if not preorder or not inorder:
            return None
        
        #create an index that will iterate through preorder
        self.pre_idx = 0

        #create a dictionary to hold the value and idx of inorder, for O(1) lookup
        self.idx_map = {}
        for i, val in enumerate(inorder):
            self.idx_map[val] = i
        
        def build(left, right):
            if left > right:
                return None
            
            node_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(node_val)

            #find the idx of the root node of the subtree within inorder
            mid = self.idx_map[node_val]

            #the left subtree of the node goes from left -> mid-1
            node.left = build(left, mid-1)
            #the right subtree starts from mid+1 to the right
            node.right= build(mid+1, right)

            return node
        
        return build(0, len(inorder)-1)