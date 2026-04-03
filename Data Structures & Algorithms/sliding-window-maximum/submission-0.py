class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = deque()

        for i in range(k):
            while maxes and maxes[-1] < nums[i]:
                maxes.pop()
            maxes.append(nums[i])

        res = [maxes[0]]

        left = 0
        right = k
        while right != len(nums):
            if maxes[0] == nums[left]:
                maxes.popleft()
            left += 1
            while maxes and maxes[-1] < nums[right]:
                maxes.pop()
            maxes.append(nums[right])

            res.append(maxes[0])
            right += 1

        return res