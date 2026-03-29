class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for rowInd in range(rows):
            nextSpot = cols - 1
            for colInd in range(cols - 1, -1, -1):
                if boxGrid[rowInd][colInd] == '#':
                    tmp = boxGrid[rowInd][nextSpot]
                    boxGrid[rowInd][nextSpot] = boxGrid[rowInd][colInd]
                    boxGrid[rowInd][colInd] = tmp
                    nextSpot -= 1
                if boxGrid[rowInd][colInd] == '*':
                    nextSpot = colInd - 1
        
        rotated = []
        for _ in range(cols):
            rotated.append([''] * rows)
        
        for colInd in range(cols):
            for rowInd in range(rows - 1, -1 ,-1):
                rotated[colInd][rows - 1 - rowInd] = boxGrid[rowInd][colInd]

        return rotated
