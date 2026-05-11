class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDist = float("inf")
        ind1 = float("inf")
        ind2 = float("inf")
        for index, word in enumerate(wordsDict):
            if word == word1:
                ind1 = index
            elif word == word2:
                ind2 = index
            minDist = min(minDist, abs(ind1 - ind2))

        return minDist