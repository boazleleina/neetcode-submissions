class Solution:
    def isValid(self, s: str) -> bool:
        #create hashmap for parantheses, with closing bracket as key
        key_map = {')':'(', '}':'{' ,']':'['}
        #initiate stack
        paranth_stack = []

        #loop through the string:
        for ch in s:
            #if the current character is a closing bracket:
            if ch in key_map:
                #if the stack is empty or top doesn't match return false
                if not paranth_stack or key_map[ch] != paranth_stack[-1]:
                    return False
                #else pop the top item
                else:
                    paranth_stack.pop()
            #else append the open bracket
            else:
                paranth_stack.append(ch)
        #return True if stack empty
        return not paranth_stack