# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr is not None:
            while curr.next is not None and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next

        return head
