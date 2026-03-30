class UnionFind:
    def __init__(self):
        self.parents = defaultdict()
        self.sizes = defaultdict()
        self.count = 0

    def addIsland(self, pos):
        if pos in self.parents:
            return
        self.parents[pos] = pos
        self.sizes[pos] = 1
        self.count += 1
    
    def isIsland(self, pos):
        return pos in self.parents

    def numIslands(self):
        return self.count
    
    def find(self, pos):
        while pos != self.parents[pos]:
            self.parents[pos] = self.parents[self.parents[pos]]
            pos = self.parents[pos]
        return pos

    def union(self, pos1, pos2):
        if not self.isIsland(pos1) or not self.isIsland(pos2):
            return

        p = self.find(pos1)
        q = self.find(pos2)
        if p == q:
            return

        if self.sizes[p] >= self.sizes[q]:
            self.parents[q] = p
            self.sizes[p] += self.sizes[q]
        else:
            self.parents[p] = q
            self.sizes[q] += self.sizes[p]
        self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        islandUnion = UnionFind()
        for position in positions:
            island = tuple(position)
            islandUnion.addIsland(island)

            islandUnion.union(island, (island[0] - 1, island[1]))
            islandUnion.union(island, (island[0] + 1, island[1]))
            islandUnion.union(island, (island[0], island[1] - 1))
            islandUnion.union(island, (island[0], island[1] + 1))

            result.append(islandUnion.numIslands())

        return result

