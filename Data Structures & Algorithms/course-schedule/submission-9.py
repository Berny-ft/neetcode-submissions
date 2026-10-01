class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 means un checked ,1 means currently cecking, 2 means safe
        
        state = [0] * numCourses # this only works because courses are ints so we can index them in the stae as well 
        # oh but i can't make them numbers because courses are also nuumbers so that is why we use colors, ACUTALLY  colors are attached to numbers so its not aobut the number it self lol its just about its index

        def dfs(course):
            state[course] = 1

            for pre in graph[course]:
                if state[pre] == 1:
                    return False
                if state[pre] == 0 and not dfs(pre):
                    return False
                
            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0 and not dfs(course):
                return False
        return True

        