class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boards = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                current = board[i][j]
                if current == ".":
                    continue
                if current in rows[i]:
                    return False
                rows[i].add(current)
                if current in cols[j]:
                    return False
                cols[j].add(current)
                currentBoard = (i // 3, j // 3)
                if current in boards[currentBoard]:
                    return False
                boards[currentBoard].add(current)

        return True