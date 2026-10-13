class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [ i for i in range(n)]


        def find(x):
            while parent[x] != x : # the current node is not its own parent
                x = parent[x]
            return x

        def union(a,b):
            ra, rb = find(a), find(b)

            if ra != rb :# they have different parents
                parent[rb] = ra
            
        for s,d in edges:
            union(s,d)

        uniques = set()
        for i in parent:
            uniques.add(find(i))

        return len(uniques)        