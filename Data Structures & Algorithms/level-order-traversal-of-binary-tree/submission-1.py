# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #create a queue
        q = collections.deque()
        #create result, to hold the levels in sublists
        res = []
        #insert the root to the queue
        q.append(root)
        #loop until the queue is empty
        while q:
            #create the sublist
            sublist = []
            #get the length of the queue
            qLen = len(q)
            #loop through the range of this length
            for i in range(qLen):
                #pop the item from the front of the queue
                node = q.popleft()
                #append it to the sublist
                if node:
                    sublist.append(node.val)
                    #get its children and add them to the back of the queue
                    q.append(node.left)
                    q.append(node.right)
            #append the sublist to the res list
            if sublist:
                res.append(sublist)
        
        #return the result list
        return res
           