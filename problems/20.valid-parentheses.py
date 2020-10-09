class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"[": "]", "(": ")", "{": "}"}
        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                opening = stack.pop()

                if mapping[char] != opening:
                    return False

        return len(stack) != 0
