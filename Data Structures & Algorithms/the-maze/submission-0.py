class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def outOfBounds(r, c):
            if r < 0 or c < 0:
                return True
            if r >= len(maze) or c >= len(maze[0]):
                return True
            return False

        currentPositions = [start]
        nextPositions = []
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while currentPositions:
            for currPos in currentPositions:
                if currPos[0] == destination[0] and currPos[1] == destination[1]:
                    return True

                visited.add(tuple(currPos))

                for direction in directions:
                    dirPos = currPos
                    newPos = [dirPos[0] + direction[0], dirPos[1] + direction[1]]

                    while (not outOfBounds(newPos[0], newPos[1]) and maze[newPos[0]][newPos[1]] != 1):
                        dirPos = newPos
                        newPos = [dirPos[0] + direction[0], dirPos[1] + direction[1]]
                        
                    if not tuple(dirPos) in visited:
                        nextPositions.append(dirPos)
            currentPositions = nextPositions
            nextPositions = []

        return False