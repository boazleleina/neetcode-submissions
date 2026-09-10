class Solution:
    def buildTree(self, preorder, inorder):
        #check the base case
        if not preorder or not inorder:
            return None
        #create an index to iterate through preorder
        self.pre_idx = 0

        #create a hashmap mapping value to it's index
        self.idx_map = {}
        for i, val in enumerate(inorder):
            self.idx_map[val] = i
        
        def build(left, right):
            if left > right:
                return None
            
            rootval = preorder[self.pre_idx]
            self.pre_idx += 1
            rootnode = TreeNode(rootval)

            #this will give me the idx of the root of the subtree
            mid = self.idx_map[rootval]

            rootnode.left = build(left, mid-1)
            rootnode.right = build(mid+1, right)

            return rootnode
        
        return build(0, len(inorder)-1)

