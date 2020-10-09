class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

    def lengthOfLastWordNotNice(self, s: str) -> int:
        return len(([a for a in s.split(" ") if a != ""] or [""])[-1])
