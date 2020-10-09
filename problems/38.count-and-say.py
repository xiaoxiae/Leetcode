class Solution:
    def countAndSay(self, n: int) -> str:
        current = [1]

        for _ in range(n - 1):
            i = 0
            new_current = []
            while i < len(current):
                j = i
                d = current[j]

                while j < len(current) and current[j] == d:
                    j += 1

                length = j - i

                new_current += [length, d]
                i = j

            current = new_current

        return "".join(map(str, current))

    def countAndSayStr(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            i = 0
            new_current = ""
            while i < len(current):
                j = i
                d = current[j]

                while j < len(current) and current[j] == d:
                    j += 1

                length = j - i
                new_current += str(length) + str(d)
                i = j

            current = new_current

        return current
