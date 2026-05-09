class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #initiate stack
        stack = []
        #initiate array with operators
        operators = ['+', '-', '*', '/']
        #loop through tokens
        for token in tokens:
            #check if token in operators
            if token in operators:
                #assign variable 1 to stack.pop
                b = stack.pop()
                #assign varaible 2 to stack.pop
                a = stack.pop()
                #check token type and perform operation, use if-else
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    result = int(a /b)
                #stack.append(result)
                stack.append(result)
            #if it is not an operator
            else:
                #stack.append(int(token))
                stack.append(int(token))
        #return stack[-1]
        return stack[-1]