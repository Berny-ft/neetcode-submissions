class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # so you must 

        # put all the connectiosn int o an edge list then 
        # build dsu and find hte number o funique roots

        edges = []

        parent = [ i for i in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(i,len(isConnected[0])):
                if isConnected[i][j] == 1:
                    edges.append((i,j))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(a,b):
            ra,rb = find(a), find(b)

            if ra != rb:
                parent[rb] = ra
            
        for s,d in edges:
            union(s,d)

        
        uniques = set()
        for i in parent:
            root = find(i)
            if root not in uniques:
                uniques.add(root)
        return len(uniques)
        


        