class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        board = ["." * n for i in range(n)]

        boards = []
        def traverse(row):
            if row == n:
                boards.append(deepcopy(board))
                return
            for col in range(n):
                if col in cols or row + col in diag1 or col - row in diag2:
                    continue
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                cols.add(col)
                diag1.add(row + col)
                diag2.add(col - row)
                
                traverse(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(col - row)
                board[row] = board[row][:col] + "." + board[row][col + 1:]

        traverse(0)
        return boards