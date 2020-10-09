class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        table = [-1] * 256
        max_lenght = 0

        while True:
            while j < len(s) and table[ord(s[j])] == -1:
                if j - i + 1 > max_lenght:
                    max_lenght = j - i + 1

                table[ord(s[j])] = j
                j += 1

            if j == len(s):
                return max_lenght

            while i < j and table[ord(s[j])] != -1:
                table[ord(s[i])] = -1
                i += 1

            table[ord(s[j])] = j
            j += 1
