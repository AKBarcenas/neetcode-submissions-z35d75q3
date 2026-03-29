class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        targets = defaultdict(int)
        for char in t:
            targets[char] += 1
        have = 0
        need = len(targets)

        smallest = s + "1"
        left, right = 0, 0
        counts = defaultdict(int)
        while right < len(s):
            char = s[right]
            counts[char] += 1
            if char in targets and counts[char] == targets[char]:
                have += 1
            while have == need:
                if len(smallest) > len(s[left:right+1]):
                    smallest = s[left:right+1]
                char = s[left]
                counts[char] -= 1
                left += 1
                if counts[char] < targets[char]:
                    have -= 1
            right += 1
        
        if len(smallest) > len(s):
            return ""
        return smallest