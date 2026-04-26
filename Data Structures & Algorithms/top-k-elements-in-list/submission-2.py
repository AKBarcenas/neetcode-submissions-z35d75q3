class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = []
        for num in counts:
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for item in heap:
            result.append(item[1])
        return result