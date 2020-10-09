combinations = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def recursive(self, digits: str, s: str):
        if digits == "":
            if s != "":
                self.combinations_result.append(s)
        else:
            d = int(digits[0])
            for c in combinations[d]:
                self.recursive(digits[1:], s + c)

    def letterCombinations(self, digits: str) -> List[str]:
        self.combinations_result = []
        self.recursive(digits, "")
        return self.combinations_result
