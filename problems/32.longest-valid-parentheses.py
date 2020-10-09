class Solution:
    def longestValidParentheses(self, s: str) -> int:
        r"""If the current number of parentheses was a graph, we would want to get two
        points with same y, where in between the graph doesn't dip either to 0 or below
        the y (they are denoted by O in this example):

        2 |  /\
        1 | /  \/\    /\  /\
        0 |/______\__O__\/__\/O______
           01234567890123456789012345
           ((())())))(())(())()))))))
        """
        i = 0
        m = 0
        c = 0
        d = {0: 0}  # could be replaced with an array of size |s|

        for i in range(len(s)):
            if s[i] == "(":
                c += 1
                d[c] = i + 1
            elif s[i] == ")":
                c -= 1

                if c >= 0:
                    m = max(m, i - d[c] + 1)
                else:
                    c = 0
                    d[0] = i + 1

        return m
