class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def traverse(i):
            print(i)
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]

            res = 0
            if int(s[i]) > 0 and int(s[i]) < 27:
                res += traverse(i + 1)
            if i < len(s) - 1 and int(s[i:i+2]) > 0 and int(s[i:i+2]) < 27 and int(s[i]) != 0:
                res += traverse(i + 2)
            cache[i] = res
            return res

        return traverse(0)