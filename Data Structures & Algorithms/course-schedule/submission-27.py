class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # make an adjacency list

        graph = defaultdict(list)

        for c, pre in prerequisites:
            graph[c].append(pre)

        # now visite and check for cycles 
        # if a course has no prerequisites then its good to go 
        ''' 
        every time you go through all the prereques of a course and their all good 
        thn the couruse is good , while going through the prereques of a course you keep a list of the visited course if oen shows up again in the list we have a ccule and so falseo 
        '''



        def check_course(c,visiting):
            if c in visiting: return False
            if graph[c] == [] : return True

            visiting.add(c)
            for pre in graph[c]:
                if not check_course(pre,visiting):
                    return False 
                else:
                    graph[c] = []
            visiting.remove(c)
            return True

        for c in range(numCourses):
            if not check_course(c,set()):
                return False
        return True


        