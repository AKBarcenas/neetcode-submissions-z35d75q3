class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        def outOfBounds(pos):
            if pos[0] < 0 or pos[1] < 0:
                return True
            if pos[0] >= rows or pos[1] >= cols:
                return True
            return False

        currentLayer = [(start[0], start[1], 0)]
        nextLayer = []
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        seen = {}
        seen[(start[0], start[1])] = 0

        while currentLayer:
            for pos in currentLayer:
                for direction in directions:
                    curr = (pos[0], pos[1])
                    newPos = (curr[0] + direction[0], curr[1] + direction[1])
                    distance = 0
                    while not outOfBounds(newPos) and maze[newPos[0]][newPos[1]] != 1:
                        curr = newPos
                        newPos = (curr[0] + direction[0], curr[1] + direction[1])
                        distance += 1
                    
                    if (not curr in seen) or (seen[curr] > pos[2] + distance):
                        seen[curr] = pos[2] + distance
                        if curr[0] != destination[0] or curr[1] != destination[1]:
                            nextLayer.append((curr[0], curr[1], pos[2] + distance))


            currentLayer = nextLayer
            nextLayer = []

        if not (destination[0], destination[1]) in seen:
            return -1
        return seen[(destination[0], destination[1])]