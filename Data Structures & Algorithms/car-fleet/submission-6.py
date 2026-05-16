class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #zip position and speed
        #sort the array in descending order
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)
        #inititate last_time integer
        last_time = 0
        #inititate fleet integer
        fleet = 0
        #loop through the zipped array:
        for pos, spd in pos_speed:
            #calcuate time, which is (target-pos)/speed
            time = (target - pos)/ spd
            #check if last_time<time:
            if last_time < time:
                #car does not catch up, add another fleet
                fleet += 1
                #time is assigned to last_time
                last_time = time
        #return fleet
        return fleet