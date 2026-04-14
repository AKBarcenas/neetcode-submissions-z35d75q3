class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = 1

        for index in range(len(digits) - 1, -1, -1):
            if curr == 0:
                break
            
            curr += digits[index]
            digits[index] = curr % 10
            curr = curr // 10

        if curr > 0:
            digits = [curr] + digits

        return digits