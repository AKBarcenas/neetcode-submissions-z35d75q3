class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}

        def traverse(i, left):
            if left < 0:
                return False
            if i == len(s):
                return left == 0
            if (i, left) in cache:
                return cache[(i, left)]
            
            if s[i] == '(':
                cache[(i, left)] = traverse(i + 1, left + 1)
            elif s[i] == ')':
                cache[(i, left)] = traverse(i + 1, left-1)
            else:
                leftVal = traverse(i + 1, left + 1)
                rightVal = traverse(i + 1, left-1)
                emptyVal = traverse(i + 1, left)
                cache[(i, left)] = leftVal or rightVal or emptyVal

            return cache[(i, left)]
        
        return traverse(0, 0)