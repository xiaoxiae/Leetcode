class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not (s[i].isalpha() or s[i].isdigit()):
                i += 1

            while i < j and not (s[j].isalpha() or s[j].isdigit()):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

    def isPalindromeLazy(self, s: str) -> bool:
        p = "".join([c.lower() for c in s if c.isalpha() or c.isdigit()])
        return p == "".join(list(reversed(p)))
