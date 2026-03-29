class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def outOfBounds(ind):
            if ind < 0 or ind >= len(s):
                return True
            return False

        longest = ""
        for wordInd in range(len(s)):
            l = wordInd
            r = wordInd
            while not outOfBounds(l) and not outOfBounds(r) and s[l] == s[r]:
                if len(longest) < (r - l + 1):
                    longest = s[l:r+1] 
                l -= 1
                r += 1

        for wordInd in range(len(s)):
            l = wordInd
            r = wordInd + 1
            while not outOfBounds(l) and not outOfBounds(r) and s[l] == s[r]:
                if len(longest) < (r - l + 1):
                    longest = s[l:r+1]
                l -= 1
                r += 1

        return longest