class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        current = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    current.append((row, col))

        
        visited = set()

        def validPosition(pos):
            if pos[0] < 0 or pos[1] < 0:
                return False
            if pos[0] >= rows or pos[1] >= cols:
                return False
            if pos in visited:
                return False
            return True

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        nextLayer = []
        minutes = 0
        while current:
            for pos in current:
                if not validPosition(pos) or grid[pos[0]][pos[1]] == 0:
                    continue
                visited.add(pos)
                if grid[pos[0]][pos[1]] == 1:
                    fresh -= 1
                for direction in directions:
                    nextLayer.append((pos[0] + direction[0], pos[1] + direction[1]))

            if fresh == 0:
                return minutes
            current = nextLayer
            nextLayer = []
            minutes += 1

        if fresh == 0:
            return minutes

        return -1