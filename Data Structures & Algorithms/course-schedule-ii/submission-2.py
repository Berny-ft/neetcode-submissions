class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # so this is a graph problem 
        # a-b
        # b-a ; this is invalid 
        # if invalid return []
        # are are looking to do graphs and remove teh cycles
        # we ar edoing topological sort 
        # we do a and adjacnecy list for them 
        # then we explore for cycles 

        # building the list

        mapp = { course:[] for course in range(numCourses)}

        for course, pre in prerequisites:
            mapp[course].append(pre)

        output = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in mapp[course]:
                if dfs(pre) == False: # cycle 
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []


        return output
