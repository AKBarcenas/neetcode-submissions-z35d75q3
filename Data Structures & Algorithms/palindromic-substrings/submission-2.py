class Solution:
    def countSubstrings(self, s: str) -> int:
        def outOfBounds(index):
            if index < 0 or index >= len(s):
                return True
            return False
        
        count = 0
        for index in range(len(s)):
            left = index
            right = index
            while not outOfBounds(left) and not outOfBounds(right) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

            left = index
            right = index + 1
            while not outOfBounds(left) and not outOfBounds(right) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

        return count