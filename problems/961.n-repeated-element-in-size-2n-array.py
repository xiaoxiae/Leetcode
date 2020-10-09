class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        elements = set()

        for a in A:
            if a not in elements:
                elements.add(a)
            else:
                return a
