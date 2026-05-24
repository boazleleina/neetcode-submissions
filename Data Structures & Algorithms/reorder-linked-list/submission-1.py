# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        #reverse second
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev

        #interleave the two halves
        list1, list2 = head, second
        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2
