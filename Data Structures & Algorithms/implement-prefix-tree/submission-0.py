class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not char in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        
        return True