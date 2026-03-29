class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        smallest = nums[0]
        count = 0

        while left <= right:
            if nums[left] < nums[right]:
                smallest = min(smallest, nums[left])
                break

            mid = (right + left) // 2
            smallest = min(smallest, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
                count += 1

            else:
                right = mid - 1

        return smallest