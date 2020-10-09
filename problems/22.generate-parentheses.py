class Solution:
    def recursive_yield(self, n: int):
        if n == 0:
            yield ""

        for i in range(n):
            for a in self.recursive_yield(i):
                for b in self.recursive_yield(n - i - 1):
                    yield f"({a}){b}"

    def generateParenthesis(self, n: int) -> List[str]:
        return [i for i in self.recursive_yield(n)]
