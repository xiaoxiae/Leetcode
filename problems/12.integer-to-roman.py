class Solution:
    def intToRoman(self, num: int) -> int:
        table = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        result = ""
        d = 1
        while num > 0:
            rem = num % 10

            if rem == 4:
                result = table[d] + table[5 * d] + result
            elif rem == 9:
                result = table[d] + table[10 * d] + result
            elif rem < 5:
                result = table[d] * rem + result
            else:
                result = table[5 * d] + table[d] * (rem % 5) + result

            num //= 10
            d *= 10

        return result
