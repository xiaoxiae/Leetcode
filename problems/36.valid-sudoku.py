class Solution:
    def add_to_contains(self, index) -> bool:
        if index == ".":
            return False
        index = int(index) - 1

        if self.contains[index]:
            return True
        self.contains[index] = True

    def clear_contains(self):
        self.contains = contains = [False] * 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            self.clear_contains()
            for char in row:
                if self.add_to_contains(char):
                    return False

        # columns
        for i in range(len(board[0])):
            contains = [False] * 9
            for j in range(len(board)):
                char = board[j][i]

                if char != ".":
                    index = int(char) - 1

                    if contains[index]:
                        return False
                    contains[index] = True
