class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for paren in s:
            if paren == '(' or paren == '[' or paren == '{':
                seen.append(paren)
            else:
                if len(seen) < 1:
                    return False
                if paren == ')' and seen[-1] != '(':
                    return False
                if paren == ']' and seen[-1] != '[':
                    return False
                if paren == ')' and seen[-1] != '(':
                    return False
                seen.pop()

        if len(seen) > 0:
            return False

        return True