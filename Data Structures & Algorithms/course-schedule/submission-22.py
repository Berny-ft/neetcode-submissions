from functools import lru_cache
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for course,pre in prerequisites:
            graph[course].append(pre)

        
        # visitset  == all thecourses along the courr dfs path 

        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if not graph[course]:
                return True
            visitSet.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(course)
            graph[course] = []
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        
