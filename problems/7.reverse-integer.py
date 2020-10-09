class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        total = 0
        while x != 0:
            total = total * 10 + x % 10
            x //= 10

        if total > (2 ** 31 - 1) or total < (-(2 ** 31)):
            return 0

        return total * sign
