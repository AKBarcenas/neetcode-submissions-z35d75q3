class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()

        def visit(pos, visited, lastHeight):
            if pos in visited:
                return
            
            if pos[0] < 0 or pos[0] > len(heights) - 1 or pos[1] < 0 or pos[1] > len(heights[0]) - 1:
                return

            if heights[pos[0]][pos[1]] < lastHeight:
                return
            
            visited.add(pos)
            visit((pos[0] - 1, pos[1]), visited, heights[pos[0]][pos[1]])
            visit((pos[0] + 1, pos[1]), visited, heights[pos[0]][pos[1]])
            visit((pos[0], pos[1] - 1), visited, heights[pos[0]][pos[1]])
            visit((pos[0], pos[1] + 1), visited, heights[pos[0]][pos[1]])

        for i in range(len(heights)):
            visit((i,0), pacific, heights[i][0])
        for j in range(len(heights[0])):
            visit((0,j), pacific, heights[0][j])
        for i in range(len(heights)):
            visit((i,len(heights[0]) - 1),atlantic,heights[i][len(heights[0]) - 1])
        for j in range(len(heights[0])):
            visit((len(heights) - 1,j),atlantic,heights[len(heights) - 1][j])

        results = []
        for entry in pacific:
            if entry in atlantic:
                results.append(entry)
        return results
            