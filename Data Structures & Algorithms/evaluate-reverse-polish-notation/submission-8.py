class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if stack:
                    b = stack.pop()
                    a = stack.pop()
                    if token == "+":
                        result = a + b
                    elif token == "-":
                        result = a - b
                    elif token == "*":
                        result = a * b
                    elif token == "/":
                        result = int(a/b)
                    stack.append(result)
        return stack[-1]
            