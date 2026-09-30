class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create a map to hold the prereqs and the courses that depend on it
        prereq = defaultdict(list)

        #map the prereq to the courses
        for course in prerequisites:
            prereq[course[1]].append(course[0])

        #create a set to keep track of our current path
        current_path = set()

        #keep track of courses I can finish
        safe_courses = set()

        #create a list for our result
        res = []

        #recurse through the course and its neighbors to check that it is valid
        def dfs(course):
            if course in current_path:
                return False
            
            if course in safe_courses:
                return True

            current_path.add(course)

            for nei in prereq[course]:
                if not dfs(nei):
                    return False
            
            safe_courses.add(course)
            res.append(course)

            current_path.remove(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res[::-1]