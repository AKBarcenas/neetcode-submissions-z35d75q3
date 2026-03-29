class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for index in range(len(word)):
                char = word[index]
                if not char in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True

        rows = len(board)
        cols = len(board[0])
        visited = set()
        found = set()

        def outOfBounds(row, col, gridRow, gridCol):
            if row < 0 or col < 0:
                return True
            if row >= gridRow or col >= gridCol:
                return True
            return False

        def traverse(row, col, trie, word):
            if outOfBounds(row, col, rows, cols):
                return

            if (row, col) in visited:
                return

            currentChar = board[row][col]
            if not currentChar in trie.children:
                return
            
            visited.add((row,col))
            word.append(currentChar)
            newTrie = trie.children[currentChar]
            if newTrie.endOfWord:
                found.add("".join(word))

            traverse(row - 1, col, newTrie, word)
            traverse(row + 1, col, newTrie, word)
            traverse(row, col - 1, newTrie, word)
            traverse(row, col + 1, newTrie, word)
            visited.remove((row,col))
            word.pop()

        for rInd in range(rows):
            for cInd in range(cols):
                traverse(rInd, cInd, root, [])

        return list(found)