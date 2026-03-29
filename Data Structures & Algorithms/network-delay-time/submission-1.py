class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgeMap = defaultdict(list)
        for time in times:
            #if not time[0] in edgeMap:
                #edgeMap[time[0]] = []
            edgeMap[time[0]].append((time[1], time[2]))

        currentEdges = [(0, k)]
        visited = {}

        while currentEdges:
            time, node = heapq.heappop(currentEdges)
            if node in visited:
                continue
            visited[node] = time
            #if not node in edgeMap:
                #continue
            for edge in edgeMap[node]:
                heapq.heappush(currentEdges, (time + edge[1], edge[0]))

        if len(visited) < n:
            return -1
        minTime = float("-inf")
        for node in visited:
            minTime = max(minTime, visited[node])
        return minTime