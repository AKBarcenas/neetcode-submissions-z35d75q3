class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        mins = deque()
        maxs = deque()
        longest = 0

        for right in range(len(nums)):
            while mins and nums[right] < mins[-1]:
                mins.pop()
            while maxs and nums[right] > maxs[-1]:
                maxs.pop()

            mins.append(nums[right])
            maxs.append(nums[right])

            while maxs[0] - mins[0] > limit:
                if maxs[0] == nums[left]:
                    maxs.popleft()
                if mins[0] == nums[left]:
                    mins.popleft()
                left += 1

            longest = max(longest, right - left + 1)

        return longest