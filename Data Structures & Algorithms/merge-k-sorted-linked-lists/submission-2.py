# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                
                dummy = ListNode()
                nxt= dummy

                while l1 and l2:
                    if l1.val < l2.val:
                        nxt.next = l1
                        nxt = l1
                        l1 = l1.next
                    else:
                        nxt.next = l2
                        nxt = l2
                        l2 = l2.next
                if l1:
                    nxt.next = l1
                if l2:
                    nxt.next = l2
                
                merged.append(dummy.next)
            lists = merged

        
        return lists[0] if lists else None



