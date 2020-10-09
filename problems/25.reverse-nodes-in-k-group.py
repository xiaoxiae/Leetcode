# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        head = ListNode(next=head)
        s = head
        n = head.next
        while n is not None:
            # ..-> o] -> [o -> o -> ...
            #      s      n
            #      c
            c = s
            n = c.next

            for _ in range(k):
                if n is None:
                    while c is not s:
                        # ... <- o <- o    o -> ...
                        #             c    n
                        # -------------------------
                        # ... <- o <- o    o -> ...
                        #        p    c    n
                        # -------------------------
                        # ... <- o    o -> o -> ...
                        #        p    c    n
                        # -------------------------
                        # ... <- o    o -> o -> ...
                        #        p    c
                        #             n
                        # -------------------------
                        # ... <- o    o -> o -> ...
                        #        c    n
                        p = c.next
                        c.next = n
                        n = c
                        c = p

                    return head.next

                # ... -> o -> o -> o -> ...
                #        c    n
                # -------------------------
                # ... -> o -> o -> o -> ...
                #        c    n
                #        p
                # -------------------------
                # ... -> o -> o -> o -> ...
                #        p    n
                #             c
                # -------------------------
                # ... -> o -> o -> o -> ...
                #        p    c    n
                # -------------------------
                # ... -> o <- o -> o -> ...
                #             c    n
                p = c
                c = n
                n = n.next
                c.next = p

            # ..-> o] <> [o <- o <- o]    [o ->
            #      s                c      n
            # ---------------------------------
            #             .------------.
            # ..-> o] -> [o <- o <- o] '> [o ->
            #      s                c      n
            # ---------------------------------
            #             .------------.
            # ..-> o] -> [o <- o <- o] '> [o ->
            #      s      p         c      n
            # ---------------------------------
            #             .------------.
            # ..-> o] -> [o <- o <- o] '> [o ->
            #      s      p         c      n
            #      '----------------^
            # ---------------------------------
            #             .------------.
            # ..-> o] -> [o <- o <- o] '> [o ->
            #      |      s         ^
            #      '----------------'
            # ---------------------------------

            s.next.next = n
            p = s.next
            s.next = c
            s = p

        return head.next
