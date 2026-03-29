class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        largestSeen = 0
        for num in seen:
            if num - 1 in seen:
                continue
            count = 1
            current = num + 1
            while current in seen:
                count += 1
                current += 1

            if largestSeen < count:
                largestSeen = count
        return largestSeen