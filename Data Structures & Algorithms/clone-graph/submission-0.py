"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #create a map to keep track of nodes we've already seen and their copies. Map the node to its copy
        old_to_copy = {}

        def create_copy(given_node):
            if given_node in old_to_copy:
                return old_to_copy[given_node]
            
            #create the copy
            copy = Node(given_node.val)

            #enter it to the map
            old_to_copy[given_node] = copy

            #recurse through the neighbors by looping through each individual neighbor and copying
            for neighbor in given_node.neighbors:
                copy.neighbors.append(create_copy(neighbor))
            
            return copy
        
        if node:
            return create_copy(node)
        else:
             return None
        
