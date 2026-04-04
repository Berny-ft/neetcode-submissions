"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        '''
        the general idea is that you create a large hasmap that allows you to map each of the old nodes
        to anew node that matches it with is value. then you go ahead and copy all of that nddoes 
        neighbors  having copied those neightbours using teh recursive call you pass them 
        to the copies neighbor attribute
        '''

        if not node: 
            return None # in this case there is no graph 

        
        copy_map = {}

        def dfs(curr):
            # if the current node has already been copied we return nothing 
            # the current node has to be a real node and we are trying to return its copy
            # we shoudl be visiting the smae node twice if there are no cycles
            if curr in copy_map:
                return copy_map[curr] # so we return the copy we have already computed

            copy = Node(curr.val) 
            copy_map[curr] = copy
            #then we have to call dfs to get all of that nodes neightobrs

            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)
                
        