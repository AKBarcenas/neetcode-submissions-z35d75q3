class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []
        def traverse(i):
            if i == len(s):
                result.append(current.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    current.append(s[i:j+1])
                    traverse(j+1)
                    current.pop()

        traverse(0)
        return result

    def isPalindrome(self, s):
        if len(s) % 2 == 0:
            left = 0 
            right = len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
        else:
            left = right = len(s) // 2
            while left >= 0:
                if s[left] != s[right]:
                    return False
                left -= 1
                right += 1
        return True