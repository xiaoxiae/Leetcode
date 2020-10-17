class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        Z = [0] * len(needle)

        def kmpStep(s: int, c: str):
            while needle[s] != c and s != 0:
                s = Z[s]
            if needle[s] == c:
                s = s + 1

            return s

        # build the automaton
        s = 0
        for i in range(2, len(needle)):
            s = kmpStep(s, needle[i - 1])
            Z[i] = s

        s = 0
        for i, c in enumerate(haystack):
            s = kmpStep(s, c)

            if s == len(needle):
                return i - s + 1

        return -1
