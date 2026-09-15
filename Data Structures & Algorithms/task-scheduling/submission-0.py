class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #process the most common task first since we have to keep coming back to it
        #each time find the frequent task and process it first(maxHeap)

        #create a Hashmap with the counter for each task
        taskCount = Counter(tasks)

        #create maxHeap by negating the values and then heapify
        maxHeap = [-c for c in taskCount.values()]
        heapq.heapify(maxHeap)

        #create the time variable to keep track of cycle
        time = 0
        #create queue to keep track of next availability [cnt, time+n]
        q = collections.deque()

        #loop until either the heap or queue becomes empty
        while maxHeap or q:
            #time starts adding on the each iteration
            time += 1

            #if maxHeap is not empty then pop it and reduce the count by 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                #only process cnt if it is greater than 0, otherwise the task is done
                if cnt:
                    #append to the queue and the next availabilty
                    q.append([cnt, time+n])
            
            #check if the time to process from the queue is met
            if q and q[0][1] == time:
                #append it back to the heap for next processing
                heapq.heappush(maxHeap, q.popleft()[0])
        
        #return total time after processing
        return time
