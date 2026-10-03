class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #create an adjacency list
        ticket_path = defaultdict(list)
        tickets.sort(reverse=True)
        #for each airport, get its destination in descending order
        for ticket in tickets:
            ticket_path[ticket[0]].append(ticket[1])

        res = []
        
        def dfs(ticket):
            #pop the last item in the node and recurse through it
            #While the tickets still has neighbors then recurse through it
            while ticket_path[ticket]:
                #get the smallest neighbor
                neighbor = ticket_path[ticket].pop()
                #recurse into the neighbor and keep popping until they are done
                dfs(neighbor)

            
            res.append(ticket)
            return res
        
        dfs("JFK")

        return res[::-1]



