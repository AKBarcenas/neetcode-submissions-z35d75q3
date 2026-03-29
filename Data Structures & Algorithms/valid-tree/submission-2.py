class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
        self.comps = n

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def union(self, p, q):
        p_par = self.find(p)
        q_par = self.find(q)

        if p_par == q_par:
            return False

        self.comps -= 1
        big, small = p_par, q_par
        if self.sizes[p_par] < self.sizes[q_par]:
            big, small = q_par, p_par
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]
            
        return True

        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        union = UnionFind(n)
        for src, dst in edges:
            if not union.union(src, dst):
                return False
        if union.comps != 1:
            return False
        return True