class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        curr = n
        while curr != 1:
            seen.add(curr)
            newNum = 0
            while curr != 0:
                newNum += (curr % 10) ** 2
                curr = curr // 10
            if newNum in seen:
                return False
            curr = newNum
        return True