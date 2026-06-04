# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self._khelper(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            tmp = groupPrev.next

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next

    def _khelper(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k -= 1
            if k == 0:
                return curr
        return None