class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def traverse(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i,j) in cache:
                return cache[(i,j)]

            if word1[i] == word2[j]:
                return traverse(i+1, j+1)

            add = 1 + traverse(i, j+1)
            remove = 1 + traverse(i+1, j)
            replace = 1 + traverse(i+1, j+1)

            minOperations = min(add, remove, replace)
            cache[(i,j)] = minOperations
            return minOperations

        return traverse(0, 0)