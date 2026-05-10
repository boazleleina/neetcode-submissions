class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #zip position and speed and sort in descending order
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)
        #initiate fleet
        fleet = 0
        #initiate last_time
        last_time = 0
        #loop through ordered list:
        for pos, speed in pos_speed:
            #calculate time taken for each
            time = (target-pos) / speed
            #if time > last_time:
            if time > last_time:
                #the fleet goes up by 1
                fleet += 1
                #the last_time is also updated
                last_time = time
        #return fleet
        return fleet
