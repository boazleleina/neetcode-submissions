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

        #ensure that the list is not empty
        if not head:
            return None
        
        #create copies of the nodes and wire them together
        curr = head
        while curr:
            tmp = curr.next
            copy = Node(curr.val)
            curr.next=copy
            copy.next = tmp
            curr = tmp
        
        #walk through again creating the random pointer
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        #unzip the copy from the original
        curr = head
        copy_head = head.next
        copy = copy_head
        while curr:
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
            copy = copy.next
        return copy_head
            
        