class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        i = 0
        while True:
            if len(strs[0]) <= i:
                return strs[0][:i]

            char = strs[0][i]

            for s in strs[1:]:
                if len(s) <= i or s[i] != char:
                    return strs[0][:i]

            i += 1
