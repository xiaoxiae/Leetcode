# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current_pointer, forward_pointer = head, head

        for i in range(n):
            forward_pointer = forward_pointer.next

        if forward_pointer is None:
            head = head.next
            return head

        while forward_pointer.next is not None:
            forward_pointer = forward_pointer.next
            current_pointer = current_pointer.next

        current_pointer.next = current_pointer.next.next

        return head
