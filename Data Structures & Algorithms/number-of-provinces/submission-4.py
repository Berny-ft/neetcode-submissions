class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = []

        R = len(isConnected)
        C = len(isConnected[0])
        for i in range(R):
            for j in range(i,C):
                if isConnected[i][j] == 1:
                    adj.append( (i,j) )

        

        parent = [ i for i in range(R)]


        def find(x):
            while parent[x] !=x :
                x = parent[x]
            return x

        def union(a,b):
            ra, rb = find(a), find(b)

            if  ra !=rb:
                parent[rb] = ra
        
        for s,d in adj:
            union(s,d)

        unique = set()

        for i in range(R):
            root = find(i)
            if root not in unique:
                unique.add(root)

        return len(unique)
        
        



        