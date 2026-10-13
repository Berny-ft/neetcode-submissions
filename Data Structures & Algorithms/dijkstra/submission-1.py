class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # first we creat an adjancency list that allows us to oknow for each node what are its neighbors

        adjacent = defaultdict(list)

        for s,d,w in edges:
            adjacent[s].append( (d,w) )
        
        # nwo we need to track our pairs
        shortest = {}

        heap = [ [0,src] ]

        while heap:
            w, node = heapq.heappop(heap)

            if node in shortest:
                continue
            
            shortest[node] = w

            for d,w2 in adjacent[node]:
                if  d  not in shortest:
                    heapq.heappush(heap, [ w + w2  , d])

        
        for e in range(n):
            if e not in shortest:
                shortest[e] = -1

        return shortest
