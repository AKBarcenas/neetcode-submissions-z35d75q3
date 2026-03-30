# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        row = rows - 1
        col = cols - 1
        while row >= 0 and col >= 0:
            curr = binaryMatrix.get(row, col)
            if curr == 1:
                col -= 1
            else:
                row -= 1

        if col == cols - 1:
            return -1
        return col + 1