class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def traverse(row, col, wordIndex):
            if wordIndex == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if word[wordIndex] != board[row][col] or (row,col) in visited:
                return False
            
            visited.add((row,col))
            up = traverse(row-1,col,wordIndex+1)
            down = traverse(row+1,col,wordIndex+1)
            left = traverse(row,col-1,wordIndex+1)
            right = traverse(row,col+1,wordIndex+1)
            visited.remove((row,col))
            return up or down or left or right

        for rowIndex in range(len(board)):
            for colIndex in range(len(board[0])):
                if traverse(rowIndex, colIndex, 0):
                    return True
        return False