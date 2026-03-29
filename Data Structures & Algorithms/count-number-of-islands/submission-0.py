class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    current = []
                    nextLayer = [[i,j]]
                    while nextLayer:
                        current = nextLayer
                        nextLayer = []

                        for pos in current:
                            x, y = pos[0], pos[1]
                            grid[x][y] = '0'
                            if x - 1 > -1 and grid[x - 1][y] == '1':
                                nextLayer.append([x - 1, y])
                            if x + 1 < len(grid) and grid[x + 1][y] == '1':
                                nextLayer.append([x + 1, y])
                            if y - 1 > -1 and grid[x][y - 1] == '1':
                                nextLayer.append([x, y - 1])
                            if y + 1 < len(grid[0]) and grid[x][y + 1] == '1':
                                nextLayer.append([x, y + 1])
        return islands