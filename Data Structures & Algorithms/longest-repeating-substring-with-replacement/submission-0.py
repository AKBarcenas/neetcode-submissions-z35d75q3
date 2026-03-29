class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left, right = 0, 0
        mostFrequent = 0
        longest = 0
        while right < len(s):
            counts[s[right]] += 1
            mostFrequent = max(mostFrequent, counts[s[right]])

            while (right - left + 1) - mostFrequent > k:
                counts[s[left]] -= 1
                left += 1
                for count in counts:
                    mostFrequent = max(mostFrequent, counts[count])
            longest = max(longest, right - left + 1)
            right += 1
        return longest