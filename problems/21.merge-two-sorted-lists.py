# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 or l2

        l3 = ListNode(val=-1)  # dummy value
        c3 = l3

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                c3.next = l1
                l1 = l1.next
            else:
                c3.next = l2
                l2 = l2.next

            c3 = c3.next

        c3.next = l1 or l2
        l3 = l3.next

        return l3
