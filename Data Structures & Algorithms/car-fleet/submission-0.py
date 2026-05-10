class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #pair positions and speed of cars
        pos_speed = list(zip(position, speed))
        #sort the order using positions, from greatest to smallest
        pos_speed_sorted = sorted(pos_speed, key=lambda x:x[0], reverse=True)
        #initialize stack
        stack = []
        #loop through sorted zipped list:
        for pos, speed in pos_speed_sorted:
            #in each pair, calculate time
            time = (target-pos) / speed
            #if stack empty or time > stack[-1]:
            if not stack or time > stack[-1]:
                #stack.append(time)
                stack.append(time)
            
        #return len of stack
        return len(stack)