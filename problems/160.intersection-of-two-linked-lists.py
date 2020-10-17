# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        currA = headA
        while currA is not None:
            lenA += 1
            currA = currA.next

        lenB = 0
        currB = headB
        while currB is not None:
            lenB += 1
            currB = currB.next

        currA = headA
        currB = headB

        if lenA < lenB:
            lenA, lenB = lenB, lenA
            currA, currB = currB, currA

        for _ in range(lenA - lenB):
            currA = currA.next

        for _ in range(lenB):
            if currA == currB:
                return currA

            currA = currA.next
            currB = currB.next

# nicer solution (not mine, just one from the forum for the reference):
# class Solution:
#     # @param two ListNodes
#     # @return the intersected ListNode
#     def getIntersectionNode(self, headA, headB):
#         if headA is None or headB is None:
#             return None
#
#         pa = headA # 2 pointers
#         pb = headB
#
#         while pa is not pb:
#             # if either pointer hits the end, switch head and traverse again
#             pa = headB if pa is None else pa.next
#             pb = headA if pb is None else pb.next
#
#         return pa
#
# # the idea is if you switch head, the possible difference between length would be countered.
# # On the second traversal, they either hit or miss.
# # if they meet, pa or pb would be the node we are looking for or None
