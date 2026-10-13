class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # push skip lock push 

        adj = defaultdict(list)
        for s,d,w in edges:
            adj[s].append( (w,d))


        heap = [[0,src]]
        shortest = {}

        while heap:
            w, node = heapq.heappop(heap)

            if node in shortest:
                continue
            
            shortest[node] = w

            for w2, node2 in adj[node]:
                if node2 not in shortest:
                    heapq.heappush(heap, [ w + w2 , node2])

        for i in range(n):
            if  i not in shortest:
                shortest[i] = -1

        return shortest


