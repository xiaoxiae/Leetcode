class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        solutions = set()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        values = list(d)
        for i in range(len(d)):
            for j in range(i, len(d)):
                n1 = values[i]
                n2 = values[j]

                d[n1] -= 1
                d[n2] -= 1

                if d[n1] >= 0 and -(n1 + n2) in d and d[-(n1 + n2)] > 0:
                    solutions.add(tuple(sorted([n1, n2, -(n1 + n2)])))

                d[n1] += 1
                d[n2] += 1

        return [list(s) for s in solutions]
