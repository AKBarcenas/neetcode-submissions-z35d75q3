class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        length = 0
        counts = defaultdict(int)
        while right != len(s):
            counts[s[right]] += 1

            maxCount = 0
            for letter in counts:
                maxCount = max(maxCount, counts[letter])
            while (right - left + 1) - maxCount > k:
                counts[s[left]] -= 1
                left += 1
                for letter in counts:
                    maxCount = max(maxCount, counts[letter])
            length = max(length, right - left + 1)
            right += 1

        return length