class Solution:
    def climbStairs(self, n: int) -> int:
        """It's Fibonacci, since for n, I can either make the last step a 1 and then
        n-1, or make it a 2 and then n-2..."""
        f1, f2 = 1, 1

        for _ in range(n):
            # a trick:
            # f2 = f1 + f2
            # f1 = f2 - f1 = f1 + f2 - f1 = f2
            f2 = f1 + f2
            f1 = f2 - f1

        return f1
