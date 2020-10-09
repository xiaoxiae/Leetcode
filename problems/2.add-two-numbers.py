# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = start = ListNode()
        remainder = 0
        while l1 is not None or l2 is not None:
            curr.value = (
                (l1.val if l1 is not None else 0)
                + (l2.val if l2 is not None else 0)
                + remainder
            )

            remainder = curr.value // 10
            curr.value %= 10
            curr.next = ListNode()
            prev = curr
            curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if remainder != 0:
            curr.val = remainder
        else:
            prev.next = None

        return start
