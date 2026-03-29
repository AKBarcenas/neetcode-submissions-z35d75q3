class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)

        for prerequisite in prerequisites:
            courseMap[prerequisite[0]].append(prerequisite[1])

        visited = set()
        ordering = []
        def traverse(courseNum, currentVisited):
            if courseNum in currentVisited:
                return False
            if courseNum in visited:
                return True

            visited.add(courseNum)
            currentVisited.add(courseNum)
            for neighbor in courseMap[courseNum]:
                if not traverse(neighbor, currentVisited):
                    return False
            currentVisited.remove(courseNum)
            ordering.append(courseNum)
            return True


        for course in range(numCourses):
            if not traverse(course, set()):
                return []

        return ordering