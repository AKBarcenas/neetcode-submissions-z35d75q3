class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        res = 0
        count = 1
        for index in range(1, len(chars)):
            if chars[index] == chars[index - 1]:
                count += 1
            else:
                chars[insert] = chars[index - 1]
                insert += 1
                res += 1
                if count != 1:
                    num = []
                    while count != 0:
                        num.append(str(count % 10))
                        count = count // 10
                    for index in range(len(num) - 1, -1, -1):
                        chars[insert] = num[index]
                        res += 1
                        insert += 1
                    count = 1
        
        chars[insert] = chars[len(chars) - 1]
        insert += 1
        res += 1
        if count != 1:
            num = []
            while count != 0:
                num.append(str(count % 10))
                count = count // 10
            for index in range(len(num) - 1, -1, -1):
                chars[insert] = num[index]
                res += 1
                insert += 1
        return res