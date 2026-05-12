class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.positions = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self.positions[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        pos1 = self.positions[word1]
        pos2 = self.positions[word2]
        ind1 = 0
        ind2 = 0

        minDist = float("inf")
        while ind1 < len(pos1) and ind2 < len(pos2):
            minDist = min(minDist, abs(pos1[ind1] - pos2[ind2]))
            if pos1[ind1] < pos2[ind2]:
                ind1 += 1
            else:
                ind2 += 1

        return minDist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

