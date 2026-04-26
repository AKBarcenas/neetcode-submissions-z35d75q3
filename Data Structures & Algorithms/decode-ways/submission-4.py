class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def traverse(i):
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]

            ways = 0
            if s[i] != '0':
                ways += traverse(i + 1)
            if i <= len(s) - 2 and 10 <= int(s[i:i+2]) <= 26:
                ways += traverse(i + 2)

            cache[i] = ways
            return ways

        return traverse(0)