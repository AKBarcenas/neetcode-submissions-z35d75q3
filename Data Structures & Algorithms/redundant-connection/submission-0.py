class Union:
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}

        for num in range(n):
            self.parents[num + 1] = num + 1
            self.ranks[num + 1] = 1

    def find(self, node):
        curr = node
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr

    def union(self, node1, node2):
        p = self.find(node1)
        q = self.find(node2)

        if p == q:
            return False

        if self.ranks[p] >= self.ranks[q]:
            self.parents[q] = p
            self.ranks[p] += self.ranks[q]
        else:
            self.parents[p] = q
            self.ranks[q] += self.ranks[p]

        return True            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = Union(len(edges))

        for edge in edges:
            result = graph.union(edge[0], edge[1])

            if not result:
                return edge

        raise Exception("No valid answer found")