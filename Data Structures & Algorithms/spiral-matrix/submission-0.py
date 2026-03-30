class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        def outOfBounds(r, c):
            if r < 0 or c < 0:
                return True
            if r >= rows or c >= cols:
                return True
            return False 

        directions = [(0,1), (1,0), (0, -1), (-1,0)]
        dirInd = 0
        visited = set()
        current = (0,0)

        result = []
        while len(visited) != rows * cols:
            result.append(matrix[current[0]][current[1]])
            visited.add(current)
            direction = directions[dirInd]
            nextPos = (current[0] + direction[0], current[1] + direction[1])
            if outOfBounds(nextPos[0], nextPos[1]) or nextPos in visited:
                dirInd = (dirInd + 1) % len(directions)
                direction = directions[dirInd]
                nextPos = (current[0] + direction[0], current[1] + direction[1])
            current = nextPos
        return result