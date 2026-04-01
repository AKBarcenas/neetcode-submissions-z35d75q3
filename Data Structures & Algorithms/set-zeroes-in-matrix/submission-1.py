class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row0 = False
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row == 0:
                        row0 = True
                    else:
                        matrix[row][0] = 0
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for rInd in range(rows):
                matrix[rInd][0] = 0

        if row0:
            for cInd in range(cols):
                matrix[0][cInd] = 0
