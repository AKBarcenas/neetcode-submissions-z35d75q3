class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)

        for pre in prerequisites:
            courseMap[pre[1]].append(pre[0])
        
        visited = set()
        def traverse(course):
            if course in visited:
                return False
            visited.add(course)
            for neighbor in courseMap[course]:
                if not traverse(neighbor):
                    return False
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not traverse(course):
                return False
        return True