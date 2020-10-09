class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()

        if len(str) == 0:
            return 0

        sign = -1 if str[0] == "-" else 1
        value = 0
        for char in str[0 if str[0] not in "+-" else 1 :]:
            if char not in "0123456789":
                break

            value = value * 10 + int(char)

        value *= sign

        if value > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif value < -(2 ** 31):
            return -(2 ** 31)
        return value
