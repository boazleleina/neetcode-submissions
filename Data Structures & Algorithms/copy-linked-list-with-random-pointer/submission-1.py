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
        hash_copy = {None : None}

        original = head

        while original:
            copy = Node(original.val)
            hash_copy[original] = copy
            original = original.next
        
        original = head
        while original:
            copy = hash_copy[original]
            copy.next = hash_copy[original.next]
            copy.random = hash_copy[original.random]
            original = original.next

        return hash_copy[head]


    
    