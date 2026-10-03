class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #create an adjacency list to keep track of the neighbors
        nei_list = defaultdict(list)

        #the list will keep track of the nodes neighbors and the time it takes to reach them
        # {current_node:[neighbor, time_to_neighbor]}
        for time in times:
            nei_list[time[0]].append([time[1], time[2]])
        
        #create a minHeap that will track the current node and the time to get to it from k
        time_to_node = []

        #seed the heap with the first k and time to k, would be 0 so (0,k)
        heapq.heappush(time_to_node, (0,k))

        #create a map to keep track of the nodes we have already visited
        visited = {}


        #loop until the heap is empty
        while time_to_node:
            current_time, node = heapq.heappop(time_to_node)

            #if the node is not in visited then it is not finalized
            if node not in visited:
                #fetch the neighbors of the node
                for nei in nei_list[node]:
                    nei_time = current_time + nei[1]
                    heapq.heappush(time_to_node, (nei_time, nei[0]))
                visited[node] = current_time
        
        if len(visited) == n:
            return max(visited.values())
        return -1
