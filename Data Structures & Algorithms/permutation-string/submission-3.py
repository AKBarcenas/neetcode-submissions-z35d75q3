class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = defaultdict(int)
        for char in s1:
            counts[char] += 1

        have = 0
        need = len(counts)

        left = 0
        right = 0

        current = defaultdict(int)
        while right < len(s2):
            char = s2[right]
            current[char] += 1
            if char in counts and current[char] == counts[char]:
                have += 1

            if right - left + 1 > len(s1):
                char = s2[left]
                if char in counts and current[char] == counts[char]:
                    have -= 1
                current[char] -= 1
                left += 1
            right += 1

            if have == need:
                return True

        return False