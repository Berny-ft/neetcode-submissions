
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # you can use a counter to counter how many then sort descending and return to k 
        
        '''
        you have to map them for sure 
        then maybe you could throw dm in a max hreap and pop k times
        is that better than sorting ? well 

        '''
        table = defaultdict(int)

        for i in nums:
            table[i] += 1


        
        heap = []

        for i in table:
            heapq.heappush(heap,(-table[i], i))
        
        sol = []
        for i in range(k):
            _ , value = heapq.heappop(heap)
            sol.append(value)

        return sol



        