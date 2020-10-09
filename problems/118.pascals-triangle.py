class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        rows = [[1]]
        for i in range(numRows - 1):
            row = [1]
            for j in range(i):
                row.append(rows[-1][j] + rows[-1][j + 1])

            row.append(1)
            rows.append(row)

        return rows
