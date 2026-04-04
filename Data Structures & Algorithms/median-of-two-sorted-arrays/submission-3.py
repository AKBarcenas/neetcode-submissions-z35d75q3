class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) >= len(nums2):
            large = nums1
            small = nums2
        else:
            large = nums2
            small = nums1

        left = 0
        right = len(small) - 1

        # 
        # 4|2 6 total, 3 half
        # 4|3 7 total, 3 half
        
        while True:
            midSmall = (right + left) // 2
            midLarge = half - midSmall - 2

            smallLow = small[midSmall] if midSmall  >= 0 else float("-inf")
            smallHigh = small[midSmall + 1] if midSmall + 1 < len(small) else float("inf")
            largeLow = large[midLarge] if midLarge  >= 0 else float("-inf")
            largeHigh = large[midLarge + 1] if midLarge + 1 < len(large) else float("inf")

            if smallLow <= largeHigh and largeLow <= smallHigh:
                if total % 2 == 0:
                    return (max(smallLow, largeLow) + min(smallHigh, largeHigh)) / 2
                return min(smallHigh, largeHigh)
            elif smallLow > largeHigh:
                right = midSmall - 1
            else:
                left = midSmall + 1
    
        raise Exception("No median found")