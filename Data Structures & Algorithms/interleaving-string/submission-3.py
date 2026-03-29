class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}
        def traverse(i, j):
            print((i,j))
            if i + j == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            if (i,j) in cache:
                return cache[(i,j)]

            res = False
            if i < len(s1) and s1[i] == s3[i + j]:
                res = traverse(i + 1, j)
            if not res and j < len(s2) and s2[j] == s3[i + j]:
                res = traverse(i, j + 1)
            cache[(i,j)] = res
            return res

        return traverse(0,0)