class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {}

        for s,d,w in flights:
            adj[(s,d)] = w

        print(adj)

        table = [float('inf')] * n
        table[src] = 0 # teh cost to start is 0

        for i in range(k+1):
            table2 = table[:]
            for s,d in adj:
                if table[s] !=  float('inf') and table[s] + adj[(s,d)] < table2[d]:
                    table2[d] = table[s] + adj[(s,d)]
            
            table = table2
        
        # assuming we are guaranteed a solution 
        return table[dst] if table[dst] != float('inf') else -1


        