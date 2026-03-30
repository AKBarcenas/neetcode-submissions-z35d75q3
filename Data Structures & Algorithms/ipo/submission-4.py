class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        for project in zip(capital, profits):
            heapq.heappush(projects, project)

        count = 0
        currentCapital = w
        possibleProfits = []
        while k != count:
            while projects and projects[0][0] <= currentCapital:
                possibleProject = heapq.heappop(projects)
                heapq.heappush(possibleProfits, possibleProject[1] * -1)

            if not possibleProfits:
                break
            currentCapital += heapq.heappop(possibleProfits) * -1
            count += 1

        return currentCapital