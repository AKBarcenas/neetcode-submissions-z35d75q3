class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def outOfBounds(row, col):
            if row < 0 or col < 0:
                return True
            if row >= len(grid) or col >= len(grid[0]):
                return True
            return False

        current = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    current.append((row, col))
                    
        count = 0
        visited = set()
        while current:
            nextLayer = []
            for pos in current:
                row, col = pos[0], pos[1]
                if outOfBounds(row, col) or pos in visited or grid[row][col] == -1:
                    continue
                visited.add(pos)
                grid[row][col] = count

                directions = [(0,-1), (0,1), (-1,0), (1,0)]
                for direction in directions:
                    nextLayer.append((row + direction[0], col + direction[1]))
                
            count += 1
            current = nextLayer
                
                