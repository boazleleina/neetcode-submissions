class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #initiate empty stack
        stack = []
        #inititate output array which is zero array of len(temperatures)
        output = [0] * len(temperatures)
        #loop through temperatures:
        for i in range(len(temperatures)):
            #while the current item(i) is greater than stack[-1]:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                #pop the top of the stack
                j = stack.pop()
                #update output with the difference
                output[j] = i-j
            
            #append to the stack
            stack.append(i)

        #return output
        return output