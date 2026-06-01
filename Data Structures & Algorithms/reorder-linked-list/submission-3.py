# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Split the first and second half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #loop condition has been met
        second = slow.next
        slow.next = None
        #reverse the second half
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev
        fst, scnd = head, second
        while scnd:
            tmp1 = fst.next
            tmp2 = scnd.next
            fst.next = scnd
            scnd.next = tmp1
            fst = tmp1
            scnd = tmp2