from dataclasses import dataclass
from heapq import heapify, heappop, heappush


@dataclass
class ListNodeWrapper:
    node: ListNode

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __eq__(self, other):
        return self.node.val == other.node.val


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [ListNodeWrapper(l) for l in lists if l is not None]
        heapify(heap)
        start = current = ListNode(val=-1)  # dummy value

        while len(heap) != 0:
            element = heappop(heap)
            current.next = element.node

            element.node = element.node.next
            if element.node is not None:
                heappush(heap, element)

            current = current.next

        return start.next
