class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)

        result = []
        for req in prerequisites:
            courseMap[req[1]].append(req[0])
        
        seen = set()
        def traverse(course, curr):
            if course in curr:
                return False
            if course in seen:
                return True

            seen.add(course)
            curr.add(course)
            for neighbor in courseMap[course]:
                if not traverse(neighbor, curr):
                    return False
            curr.remove(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if not traverse(course, set()):
                return []

        result.reverse()
        return result