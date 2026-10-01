from functools import lru_cache
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we are looking for a cycle , meaning you are looking for at least a pair of courses where 1 is the prerequisite of 2 and 2 is the prerequisite of 1
        # to draft the graph you need an adjancey list  for a course you keep a lsist of its prerquisites  # so for all course add thier prequirements in a default dict list , 
        # then you must expore the dict for ducplicates 
        # you could go the thoruh list for each pair : if one is in ones prequr list the other shoudlnt be if so return false . so the time complexity is o num course  for the graph as well as 0(num course )for chekcing actual squared since is a double nested for loop to get all pairs 
        # shoudl amke the value of the dict a set instead of a list to get rid of duplicates checking tiem 


        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        WHITE, GREY, BLACK = 0,1,2
        color = [WHITE] * numCourses

        def dfs(course):
            color[course] = GREY
            for pre in graph[course]:
                if color[pre] == GREY: # we are looping
                    return False
                if color[pre] == WHITE and not dfs(pre): # we propagate the errup 
                    return False
            color[course] = BLACK
            return True

        for course in range(numCourses):
            if color[course] == WHITE and not dfs(course):
                return False
        return True

        
        