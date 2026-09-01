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

        #create the copies wired to the original
        curr = head

        while curr:
            tmp = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next = tmp
            curr = tmp
        
        # create the random pointers
        curr = head

        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        #unzip the original from the copy
        if not head:
            return None
        curr = head
        copy_head = head.next
        copy = copy_head
        while curr:
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
            copy = copy.next
        return copy_head
            
        