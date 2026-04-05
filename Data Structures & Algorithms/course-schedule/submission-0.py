class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ''' 
        you are essentially looking if there's contradiction in the prerequisite chain 
        so  [0,1] and [1,0] shoudl never exist . we could make that check first and if it fails we move on 
        but if you get a longer chain like [0,1], [1,2] , [2,3] ,[3,1]
        this is wrong since you must take 3 before 1  and also that you must take 1 before three
        this is the most complex scenario 
        so i can build a tree
        a prerequisite has is following courses below it in a hash set

        so from this chain [0,1], [1,2] , [2,3], [3,1]

        we first check all the numbers in numCourses for reqs
        
        3: { 2: {1 : { 0 } } } 

        actually this is a  bad strategy the tree is actually built from the prerequs array 
        you jus tneed to vist in such a way that you don't have loops so you can actually c

        so you can actually build an agencency list  and use it to do the dfs
        '''
        def dfs(course, visited):
            if course not in h:
                return True
            
            if course in visited:
                return False
            
            visited.append(course)
            state = True
            for p in h[course]:
                state = state and dfs(p, visited.copy())
            
            return state

        h = {}
        for p in prerequisites:
            if p[0] in h:
                h[p[0]].append(p[1])
            else:
                h[p[0]] = [ p[1] ]

        for course in h:
            if not dfs(course,[]):
                return False
        
        return True
