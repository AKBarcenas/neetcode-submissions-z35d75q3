class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        
        wordMap = defaultdict(set)

        for wordsInd in range(len(words) - 1):
            firstWord = words[wordsInd]
            secondWord = words[wordsInd + 1]
            minLen = min(len(firstWord), len(secondWord))

            for wordInd in range(minLen):
                firstChar = firstWord[wordInd]
                secondChar = secondWord[wordInd]

                if firstChar != secondChar:
                    wordMap[firstChar].add(secondChar)
                    break
                if minLen - 1 == wordInd and len(firstWord) > len(secondWord):
                    return ""

            for char in firstWord:
                if not char in wordMap:
                    wordMap[char] = set()

            for char in secondWord:
                if not char in wordMap:
                    wordMap[char] = set()
        
        visited = set()
        result = ""
        
        def traverse(char, currentVisited):
            nonlocal result
            
            if char in currentVisited:
                return False
            if char in visited:
                return True
            currentVisited.add(char)
            neighbors = wordMap[char]
            for neighbor in neighbors:
                if not traverse(neighbor, currentVisited):
                    return False
            currentVisited.remove(char)
            visited.add(char)
            result += char
            return True


        for char in wordMap:
            if not traverse(char, set()):
                return ""
        return result[::-1]
                