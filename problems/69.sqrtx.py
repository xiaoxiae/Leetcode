class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x + 1

        # invariant: lo ** 2 <= x
        while hi - lo > 1:
            avg = (lo + hi) // 2

            if avg * avg <= x:
                lo = avg
            else:
                hi = avg

        return lo
