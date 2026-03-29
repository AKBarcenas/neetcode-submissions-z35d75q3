class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allCounts = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord('a')] += 1
            allCounts[tuple(counts)].append(string)

        return list(allCounts.values())