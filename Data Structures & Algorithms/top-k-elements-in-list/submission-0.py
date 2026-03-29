class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1

        frequencies = [[] for _ in range(len(nums))]
        for num in counts:
            frequencies[counts[num] - 1].append(num)

        
        frequent = []
        for index in range(len(frequencies) - 1, -1, -1):
            frequent += frequencies[index]
            if len(frequent) == k:
                return frequent


        raise Exception("Undeterminstic answer found")