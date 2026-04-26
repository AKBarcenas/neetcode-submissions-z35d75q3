class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def traverse(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            match = 0
            if text1[i] == text2[j]:
                match = 1 + traverse(i + 1, j + 1)
            first = traverse(i + 1, j)
            second = traverse(i, j + 1)

            cache[(i, j)] = max(match, first, second)
            return cache[(i, j)]

        return traverse(0, 0)