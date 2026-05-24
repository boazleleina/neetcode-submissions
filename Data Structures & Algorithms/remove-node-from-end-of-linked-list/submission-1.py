# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Optimized method, run two pointers that are spaced out exactly
        n+1 , when the right pointer hit none ,left pointer will be n+1 behind
        """
        #in-cases where list is empty, avoid -1
        dummy = ListNode(0, head)
        left, right = dummy, dummy

        for _ in range(n+1):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
            