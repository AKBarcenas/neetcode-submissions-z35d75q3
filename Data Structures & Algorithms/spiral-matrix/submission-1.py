class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows * cols

        def outOfBounds(r, c):
            if r < 0 or c < 0:
                return True
            if r >= rows or c >= cols:
                return True
            return False
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()
        dirInd = 0

        curr = (0, 0)
        result = []
        while len(visited) != size:
            visited.add(curr)
            result.append(matrix[curr[0]][curr[1]])
            nextPos = (curr[0] + directions[dirInd][0], curr[1] + directions[dirInd][1])
            if outOfBounds(nextPos[0], nextPos[1]) or nextPos in visited:
                dirInd = (dirInd + 1) % 4
                nextPos = (curr[0] + directions[dirInd][0], curr[1] + directions[dirInd][1])
            curr = nextPos
        return result