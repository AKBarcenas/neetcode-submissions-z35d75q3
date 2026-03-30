class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for c1, c2 in prerequisites:
            courseMap[c2].append(c1)

        visited = set()
        def traverse(course):
            if course in visited:
                return False
            if not course in courseMap or not courseMap[course]:
                return True

            visited.add(course)
            neighbors = courseMap[course]
            for neighbor in neighbors:
                if not traverse(neighbor):
                    return False
            courseMap[course] = []
            visited.remove(course)
            return True

        for course in courseMap.keys():
            if not traverse(course):
                return False
        return True