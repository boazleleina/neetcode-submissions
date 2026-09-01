"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #hasmap to hold the original->copy nodes, initialize Null so it doesn't break
        nodes_copy = {None: None}

        #pass 1: create the copies in the map
        original = head

        while original:
            copy = Node(original.val)
            nodes_copy[original] = copy
            original = original.next
        
        original = head
        while original:
            copy = nodes_copy[original]
            copy.next = nodes_copy[original.next]
            copy.random = nodes_copy[original.random]
            original = original.next
        
        return nodes_copy[head]