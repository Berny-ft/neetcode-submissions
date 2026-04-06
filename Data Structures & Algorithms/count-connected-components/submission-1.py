class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        the general strategy would be to build a a list of sets

        create an ajacency list and explore it for all our nodes. in the end you get a visited list
        if that visited list is in our list of sets we've already explored it 

        do that for all the nodes we've got and in the end we return the len of the sets list 

        an optimization is that for each new value you get you go into the list of sets and first make sure
        that it isn't aredy in one of the sets. if it is you don't need to exlore again. that makes an On check for 
        each value to start with and then if isn't you have to do the tree building 

        oooh even better you actually keeep track of the nodes you've alredy seen while biulding your trees
        so that if build a set with 012 starting from 0 then i shouldn't be checking for 1 and 2 

        '''

        #build the adjacency list
        h = {}
        for left, right in edges:
            if left in h:
                h[left].append(right)
            else:
                h[left] = [right]
            if right in h:
                h[right].append(left)
            else:
                h[right] = [left]

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in h.get(node,[]):
                dfs(n)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count



        
