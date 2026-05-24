# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Brute force
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(length -n):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
            