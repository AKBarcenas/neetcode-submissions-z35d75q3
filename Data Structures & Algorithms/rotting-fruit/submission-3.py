class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def outOfBounds(r, c):
            if r < 0 or c < 0:
                return True
            if r >= rows or c >= cols:
                return True
            return False

        curr = []
        fresh = 0
        seen = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    curr.append((row, col))
                    seen.add((row, col))

        rot = 0
        count = -1
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while curr:
            nextLayer = []
            for item in curr:
                for direction in directions:
                    dirRow = item[0] + direction[0]
                    dirCol = item[1] + direction[1]
                    if outOfBounds(dirRow, dirCol) or grid[dirRow][dirCol] != 1 or (dirRow, dirCol) in seen:
                        continue
                    seen.add((dirRow, dirCol))
                    nextLayer.append((dirRow, dirCol))
                    rot += 1

            curr = nextLayer
            count += 1

        if rot == fresh:
            return max(0, count)
        return -1