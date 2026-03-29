class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counts = dict()
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        print(counts)

        for char in t:
            if char in counts:
                counts[char] -= 1
            else:
                return False
            if counts[char] < 0:
                return False
        
        for key in counts:
            if counts[key] > 0:
                return False
        return True