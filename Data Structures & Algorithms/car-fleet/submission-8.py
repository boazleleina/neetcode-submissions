class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combine the position and associated speed
        combined = sorted(zip(position, speed), reverse = True)
        #keep track of how many fleet
        fleet = 0
        #keep track of the previous time we've seen
        last_time = 0

        for pos, spd in combined:
            #find the time it takes to reach the destination
            time = (target - pos) / spd

            #new fleet if this time is slower
            if last_time < time:
                #since the time is slower this is a new fleet
                fleet += 1

                #last time is also changed to the current time
                last_time= time
        
        return fleet

    