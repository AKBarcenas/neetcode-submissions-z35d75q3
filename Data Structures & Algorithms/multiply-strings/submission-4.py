class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                current = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                result[i + j] += current % 10
                result[i + j + 1] += (current // 10) + (result[i + j] // 10)
                result[i + j] = result[i + j] % 10

        stringResult = ""

        for index in range(len(result)):
            stringResult = str(result[index]) + stringResult 

        while len(stringResult) > 1 and stringResult[0] == '0':
            stringResult = stringResult[1:]

        return stringResult