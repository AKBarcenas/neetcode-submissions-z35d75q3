class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {}
        mappings['}'] = '{'
        mappings[')'] = '('
        mappings[']'] = '['

        for char in s:
            if char in mappings.keys():
                if not stack:
                    return False
                last = stack.pop()
                if last != mappings[char]:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        return True