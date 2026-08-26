class Solution:
    def isValid(self, s: str) -> bool:
        #hashmapto check the values
        bmap = {')': '(', '}': '{', ']' : '['}
        #stack to keep track of what is added or removed
        stack = []
        #loop through the input string
        for c in s:
            #check if the character in hashmap
            if c in bmap:
                #if the stack is empty or current string doesn't match last opening string
                #return false
                if not stack or stack[-1] != bmap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0
                