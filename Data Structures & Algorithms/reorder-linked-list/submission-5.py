# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Break the list into two halves
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # 2. Reverse the second half
        prev, curr = None, second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        fst, scd = head, prev

        #3. Merge while alternating
        while scd:
            tmp1 = fst.next
            tmp2 = scd.next
            fst.next = scd
            scd.next = tmp1
            fst = tmp1
            scd = tmp2
        
