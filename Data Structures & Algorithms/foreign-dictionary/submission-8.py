class Solution:
    def getLetter(self, word1, word2):
        length = min(len(word1), len(word2))
        for index in range(length):
            if word1[index] != word2[index]:
                return index
        if len(word1) > len(word2):
            return -1
        return -2

    def foreignDictionary(self, words: List[str]) -> str:
        charMap = defaultdict(list)
        for word in words:
            for char in word:
                charMap[char] = []

        for index in range(len(words) - 1):
            letter = self.getLetter(words[index], words[index + 1])
            if letter == -1:
                return ""
            if letter == -2:
                continue
            charMap[words[index][letter]].append(words[index + 1][letter])

        result = []
        allVisited = set()

        def traverse(char, visited):
            if char in visited:
                return False
            if char in allVisited:
                return True
            allVisited.add(char)
            visited.add(char)

            if char in charMap:
                for neighbor in charMap[char]:
                    if not traverse(neighbor, visited):
                        return False
            
            visited.remove(char)
            result.append(char)
            return True
            
        for char in charMap:
            if not traverse(char, set()):
                return ""

        dictionary = "".join(reversed(result))
        return dictionary