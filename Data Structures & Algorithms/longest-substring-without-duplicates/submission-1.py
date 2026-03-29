class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right = 0, 0
        seen = defaultdict(int)
        maxLength = 0
        seen[s[left]] += 1
        while right < len(s):
            maxLength = max(maxLength, right - left + 1)
            right += 1
            if not right < len(s):
                return maxLength

            seen[s[right]] += 1
            while seen[s[right]] > 1 and left != right:
                seen[s[left]] -= 1
                left += 1
        return maxLength
