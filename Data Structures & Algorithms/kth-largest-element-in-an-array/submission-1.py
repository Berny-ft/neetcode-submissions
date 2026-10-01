import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # no sorting 
        # throw them all in a heap and pop k times return the inverse of the vlaue you put ? 
        # no need to track uniticy since it isnt a requiement
        h = []
        for i in nums:
            heapq.heappush(h, -i)

        for i in range(k-1):
            heapq.heappop(h)

        return -heapq.heappop(h)
        

        