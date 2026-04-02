class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}

        def traverse(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            possible = False
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    possible = possible or traverse(j + 1)
            cache[i] = possible
            return possible
        return traverse(0)