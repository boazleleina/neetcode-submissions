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
        copy_map = {None:None}
        original = head

        while original:
            copy_map[original] = Node(original.val)
            original = original.next

        original = head

        while original:
            copy = copy_map[original]
            copy.next = copy_map[original.next]
            copy.random = copy_map[original.random]
            original = original.next
        
        return copy_map[head]

