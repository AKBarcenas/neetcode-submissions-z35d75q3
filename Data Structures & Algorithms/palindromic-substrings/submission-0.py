class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def outOfBounds(ind):
            if ind < 0 or ind >= len(s):
                return True
            return False

        res = 0
        for wordInd in range(len(s)):
            l = wordInd
            r = wordInd
            while not outOfBounds(l) and not outOfBounds(r) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for wordInd in range(len(s)):
            l = wordInd
            r = wordInd + 1
            while not outOfBounds(l) and not outOfBounds(r) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res