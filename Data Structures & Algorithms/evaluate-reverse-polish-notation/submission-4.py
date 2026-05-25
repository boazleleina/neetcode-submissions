class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #initiate array of operators
        operators = ["+", "-", "*", "/"]
        #initiate stack to hold operands and result
        operands = []
        #loop through each token in tokens:
        for token in tokens:
            #if the token is an operator(meaning it is array) and stack is not empty:
            if token in operators:
                if len(operands)<2:
                    raise ValueError("Not enough operands for the operator")
                #pop the top item in stack first item popped will be second in operation
                b = operands.pop()
                #second item popped will be first in the operation
                a = operands.pop()
                #use an elif statement to loop through each operator
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    result = int(a / b)
                #append result in the stack
                operands.append(result)
            #append item to stack
            else:
                operands.append(int(token))
        return operands[-1]