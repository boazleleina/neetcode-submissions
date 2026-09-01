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

        if not head:
            return None
        
        #create hashmap to hold the values
        nodes_copy = {}

        #pass 1 create copies in the hashmap
        original = head

        while original:
            copy = Node(original.val)
            nodes_copy[original] = copy
            original = original.next
        
        #pass 2 map the pointers using the map
        original = head
        while original:
            copy = nodes_copy[original]
            copy.next = nodes_copy[original.next] if original.next else None
            copy.random = nodes_copy[original.random] if original.random else None
            original = original.next
        
        return nodes_copy[head]