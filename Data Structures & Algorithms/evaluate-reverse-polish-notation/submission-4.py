class Solution:
    def evalRPN(self, tokens: List[str]) -> int:     
        operands = ['+', '-', '*', '/']

        stack = []

        for index in range(len(tokens)):
            token = tokens[index]
            if token in operands:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    second = first + second
                elif token == '-':
                    second = first - second
                elif token == '*':
                    second = first * second
                elif token == '/':
                    second = first / second
                    if second < 0:
                        second = math.ceil(second)
                    elif second > 0:
                        second = math.floor(second)
                stack.append(second)
            else:
                stack.append(int(token))
            print(stack)

        return int(stack[0])