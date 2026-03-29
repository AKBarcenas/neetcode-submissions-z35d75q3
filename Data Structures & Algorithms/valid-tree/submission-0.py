class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = defaultdict(list)
        for n1, n2 in edges:
            edgeMap[n1].append(n2)
            edgeMap[n2].append(n1)

        visited = set()
        def traverse(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for neighbor in edgeMap[curr]:
                if neighbor == prev:
                    continue
                if not traverse(neighbor, curr):
                     return False
            return True

        if not traverse(0, -1):
             return False
        return len(visited) == n