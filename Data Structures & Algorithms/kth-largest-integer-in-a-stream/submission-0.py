class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.stream = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)

        if len(self.stream) > self.size:
            heapq.heappop(self.stream)

        return self.stream[0]