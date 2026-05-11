class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #append item to stack
        self.stack.append(val)
        #if minstack is empty append
        if not self.minStack:
            self.minStack.append(val)
        #else compare top value in minStack and current value and append the min
        else:
            min_val = min(self.minStack[-1], val)
            self.minStack.append(min_val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
