class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def outOfBounds(pos):
            if pos[0] < 0 or pos[1] < 0:
                return True
            if pos[0] >= rows or pos[1] >= cols:
                return True
            return False

        def visit(pos):
            if outOfBounds(pos) or pos in visited or board[pos[0]][pos[1]] == "X":
                return

            visited.add(pos)
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for direction in directions:
                visit((pos[0] + direction[0], pos[1] + direction[1]))

        for col in range(cols):
            visit((0, col))
            visit((rows - 1, col))

        for row in range(rows):
            visit((row, 0))
            visit((row, cols - 1))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X" or (row, col) in visited:
                    continue
                board[row][col] = "X"