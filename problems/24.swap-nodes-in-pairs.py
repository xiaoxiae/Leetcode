# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head = ListNode(next=head)  # dummy node
        curr = head
        while True:
            # return if there are <2 elements
            if curr.next is None or curr.next.next is None:
                return head.next

            # reverse nodes
            a = curr.next
            b = curr.next.next.next

            curr.next = curr.next.next
            curr.next.next = a
            a.next = b

            # move by 2
            curr = curr.next.next

        return head.next
