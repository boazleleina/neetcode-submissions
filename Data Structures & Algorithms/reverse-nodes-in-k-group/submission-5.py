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

            kth_node = groupPrev
            for i in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    break
            
            if not kth_node:
                break

            groupNext = kth_node.next

            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth_node
            groupPrev = tmp
        
        return dummy.next
            
