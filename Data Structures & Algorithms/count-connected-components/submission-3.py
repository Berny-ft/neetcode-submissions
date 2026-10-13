class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a,b):
            ra, rb = find(a) , find(b)
            if ra== rb:
                return False
            parent[rb] = ra
            return True

        for s,d in edges:
            union(s,d)
        
        uniques = set()
        for i in parent:
            uniques.add(find(i))
        return len(uniques)