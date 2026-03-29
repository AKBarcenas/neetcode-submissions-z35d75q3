class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not char in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def traverse(curr, word):
            if len(word) < 1:
                return curr.endOfWord
            if len(curr.children) < 1:
                return False

            currentChar = word[0]
            if currentChar == '.':
                found = False
                for char in curr.children:
                    found = found or traverse(curr.children[char], word[1:])
                return found
            else:
                if not currentChar in curr.children:
                    return False
                return traverse(curr.children[currentChar], word[1:])

        return traverse(self.root, word)