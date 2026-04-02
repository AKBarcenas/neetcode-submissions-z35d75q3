class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        usedTasks = deque()
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1

        time = 0
        heap = []
        for count in counts.values():
            heap.append(count * -1)
        heapq.heapify(heap)

        while heap or usedTasks:
            while usedTasks and time - usedTasks[0][1] > n:
                task = usedTasks.popleft()
                heapq.heappush(heap, task[0] * -1)

            if heap:
                curr = heapq.heappop(heap)
                if curr * -1 - 1 > 0:
                    usedTasks.append((curr * -1 - 1, time))

            time += 1

        return time