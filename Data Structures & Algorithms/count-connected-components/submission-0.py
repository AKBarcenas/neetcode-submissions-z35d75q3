class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(node):
            curr = node
            while curr != parents[curr]:
                curr = parents[curr]
            return curr

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return 0
            if ranks[parent1] > ranks[parent2]:
                ranks[parent1] += ranks[parent2]
                parents[parent2] = parent1
            else:
                ranks[parent2] += ranks[parent1]
                parents[parent1] = parent2
            return -1

        result = n
        for e1, e2 in edges:
            result += union(e1, e2)
        return result