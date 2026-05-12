class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) - len(self.minHeap) > 1:
            element = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -element)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            element = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -element)

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]