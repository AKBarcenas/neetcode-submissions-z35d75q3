class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = defaultdict(list)
        for first, second in prerequisites:
            nodes[first].append(second)

        def traverse(node):
            if node in visited:
                return False
            if not node in nodes or not nodes[node]:
                return True
            visited.add(node)
            for neighbor in nodes[node]:
                if not traverse(neighbor):
                    return False
            #nodes[node] = []
            visited.remove(node)
            return True

        for node in nodes:
            visited = set()
            if not traverse(node):
                return False


        return True