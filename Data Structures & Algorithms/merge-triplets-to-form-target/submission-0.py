class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = False, False, False
        for triplet in triplets:
            if target[0] == triplet[0] and target[1] >= triplet[1] and target[2] >= triplet[2]:
                x = True
            if target[1] == triplet[1] and target[0] >= triplet[0] and target[2] >= triplet[2]:
                y = True
            if target[2] == triplet[2] and target[0] >= triplet[0] and target[1] >= triplet[1]:
                z = True

        return x and y and z