from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        if rowIndex == 0:
            return row

        for i in range(rowIndex + 1):
            nrow = [1]
            for j in range(i - 1):
                nrow.append(row[j] + row[j + 1])
            nrow.append(1)

            row = nrow

        return row
