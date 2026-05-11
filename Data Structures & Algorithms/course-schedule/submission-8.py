class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)

        for pre in prerequisites:
            courseMap[pre[1]].append(pre[0])
        
        visited = set()
        def traverse(course, curr):
            if course in curr:
                return False
            if course in visited:
                return True
            curr.add(course)
            visited.add(course)
            for neighbor in courseMap[course]:
                if not traverse(neighbor, curr):
                    return False
            return True

        for course in range(numCourses):
            if not traverse(course, set()):
                return False
        return True