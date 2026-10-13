class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list) # we have to define connections 
        for s,d,w in times:
            adj[s].append( (w,d))

        heap = [[0,k]]
        shortest = {}


        while heap:
            w , node = heapq.heappop(heap)
            if node in shortest:
                continue
            
            shortest[node] = w

            for w2,node2 in adj[node]:
                if node2 not in shortest:
                    heapq.heappush(heap, [w2+w, node2])
            
        maximum = 0
        for i in range(1,n+1):
            if i not in shortest:
                return -1
            maximum = max(shortest[i],maximum)

        return maximum
        


        