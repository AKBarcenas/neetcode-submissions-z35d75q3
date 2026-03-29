class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right and (numbers[left] + numbers[right]) != target:
            if target < numbers[left] + numbers[right]:
                right -= 1
            else:
                left += 1
        
        if not left < right:
            raise Exception("No valid solution found")

        return [left + 1, right + 1]