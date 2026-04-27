class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ind1 = -1
        ind2 = -1
        minDist = float("inf")
        for index in range(len(wordsDict)):
            if word1 == wordsDict[index]:
                ind1 = index
            if word2 == wordsDict[index]:
                ind2 = index
            if ind1 != -1 and ind2 != -1:
                minDist = min(minDist, abs(ind1 - ind2))

        return minDist