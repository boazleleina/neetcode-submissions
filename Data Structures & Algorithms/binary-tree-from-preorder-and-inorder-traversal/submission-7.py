class Solution:
    def buildTree(self, preorder, inorder):
        #check for the base case
        if not preorder or not inorder:
            return None
        
        #get an index counter to walk through preorder
        self.pre_idx = 0

        #create a hashmap with values and index in inorder
        self.ind_map = {}
        for i, val in enumerate(inorder):
            self.ind_map[val] = i
        
        def build(left, right):
            if left > right:
                return None
            
            node_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(node_val)

            mid = self.ind_map[node_val]
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)

            return node
        
        return build(0, len(inorder)-1)

