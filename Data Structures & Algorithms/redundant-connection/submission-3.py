class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # we have n does
        parent =[ i for i in range(len(edges)+1)]
        
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a,b):
            ra, rb = find(a), find(b)

            if ra == rb: # this is the node node too many 
                return True
            
            parent[rb] = ra

            return False
        
        for s,d in edges:

            if union(s,d):
                return [s,d]
