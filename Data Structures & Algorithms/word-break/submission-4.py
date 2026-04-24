class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def traverse(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            result = False
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    result = traverse(i + len(word))
                    if result:
                        return True
                
            cache[i] = result
            return result
            
        return traverse(0)