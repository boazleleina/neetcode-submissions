# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self._mergehelper(l1, l2))
            lists = merged_list
        return lists[0]



    def _mergehelper(self, l1, l2):
        dummy = ListNode(0)
        start = dummy

        while l1 and l2:
            if l1.val < l2.val:
                start.next = l1
                start = l1
                l1 = l1.next
            else:
                start.next = l2
                start = l2
                l2 = l2.next
        if l1:
            start.next = l1
        else:
            start.next = l2
        
        return dummy.next






