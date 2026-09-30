class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a hashmap mapping the prereqs to the courses it supports
        prereqs = defaultdict(list)

        #create a set to keep the current path I am exploring
        current_path = set()

        #create a set to keep the courses that can be successfully finished, no cycle
        safe_courses = set()

        #map the prereqs to the courses that need it
        for course in prerequisites:
            prereqs[course[1]].append(course[0])
        
        #do a dfs to recurse through the neighbors
        def dfs(course):
            #if I have already seen the course in the path, then it's a cycle
            if course in current_path:
                return False

            #if the course makes it to the safe course then no cycle and can be done
            if course in safe_courses:
                return True
            
            current_path.add(course)

            #recurse through the neighbors and check if they are safe
            for nei in prereqs[course]:
                #if it finds a cycle then immediately return False
                if not dfs(nei):
                    return False
            
            #it passed through the catch, so add the course to safe
            safe_courses.add(course)

            #now remove from current path to go to the next path
            current_path.remove(course)

            #the course passed all checks so it can be done
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True