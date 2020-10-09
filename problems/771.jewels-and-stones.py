class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for char in S:
            if char in J:
                total += 1

        return total
