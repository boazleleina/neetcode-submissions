# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        nxt = dummy

        while list1 and list2:
            if list1.val < list2.val:
                nxt.next = list1
                nxt = list1
                list1 = list1.next
            else:
                nxt.next = list2
                nxt = list2
                list2 = list2.next
        
        if list1:
            nxt.next = list1
        if list2:
            nxt.next = list2

        return dummy.next

