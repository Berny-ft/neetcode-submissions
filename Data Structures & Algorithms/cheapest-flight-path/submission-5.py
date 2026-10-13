class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        table = [ float('inf') for _ in range(n)]

        table[src] = 0

        for i in range(k+1):

            table2 = table[:]

            for i in flights:
                s,d,w = i # we get all edges

                '''
                for each pair we are loooking to see if the distanc eis less than infinity 
                or if it is less than what it is currenlty, less than it currenlty is is less then infity
                '''
                if table[s] != float('inf') and table[s] + w < table2[d]:
                    table2[d] = table[s] + w

            table  = table2
        
        return  table[dst] if table[dst] < float('inf') else -1
        