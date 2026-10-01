from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for course,pre in prerequisites:
            graph[course].append(pre)

        state= [0] * numCourses
        sol = []

        def dfs(course):
            state[course] = 1
            for pre in graph[course]:
                if state[pre] == 1:
                    return False
                if state[pre] == 0 and not dfs(pre):
                    return False
            
            state[course] = 2
            sol.append(course)
            return True
        
        for course in range(numCourses):
            if state[course] == 0 and not dfs(course):
                return []
        return sol

        