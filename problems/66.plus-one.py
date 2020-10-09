class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        i = len(digits) - 1
        while i >= 0 and remainder == 1:
            digits[i] += remainder
            remainder = digits[i] // 10
            digits[i] %= 10

            i -= 1

        if remainder == 1:
            digits = [remainder] + digits

        return digits

