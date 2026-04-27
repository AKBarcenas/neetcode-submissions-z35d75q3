class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.distances = {}
        for i in range(len(wordsDict)):
            for j in range(i + 1, len(wordsDict)):
                if wordsDict[i] == wordsDict[j]:
                    continue
                key = sorted([wordsDict[i], wordsDict[j]])
                if (key[0], key[1]) in self.distances:
                    self.distances[(key[0], key[1])] = min(self.distances[(key[0], key[1])], j - i)
                else:
                    self.distances[(key[0], key[1])] = j - i

    def shortest(self, word1: str, word2: str) -> int:
        key = sorted([word1, word2])
        return self.distances[(key[0], key[1])]


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
