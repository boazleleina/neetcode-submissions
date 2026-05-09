class Solution:
    def isValid(self, s: str) -> bool:
        #instantiate a stack
        stack = []
        #instantiate a map to map opening to close
        brackMap = {")":"(", "}":"{", "]": "["}

        #loop through ch in s:
        for ch in s:
            #check if ch is in map
            if ch in brackMap:
                #return false if stack is empty or top item in stack does not map the current ch
                if not stack or stack[-1] != brackMap[ch]:
                    return False
                #pop items from the stack
                stack.pop()
            else:
                #it is an opening bracket so add it to stack
                stack.append(ch)
        
        #return True if the stack is empty
        return len(stack) == 0
