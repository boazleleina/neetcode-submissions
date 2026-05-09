class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #instantiate indices stack
        stack = []
        #instantiatiate result array to store all the results
        results = [0] * len(temperatures)

        #loop through the temperatures: 
        for i in range(len(temperatures)):
            #check while stuck is not empty and the current temperature is greater than the top item in the stack:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                #pop the top item
                j = stack.pop()
                #enter the result into the result at the i index of result
                results[j] = i - j
     
            #append the item to the empty stack
            stack.append(i)
        #return results
        return results
        