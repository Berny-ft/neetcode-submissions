import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # no sorting 
        # throw them all in a heap and pop k times return the inverse of the vlaue you put ? 
        # no need to track uniticy since it isnt a requiement
        h = []


        for i in range(k):
            heapq.heappush(h,nums[i])

        
        for i in range(k, len(nums)):
            if h[0] < nums[i]:
                heapq.heappop(h)
                heapq.heappush(h,nums[i])

        return h[0]

       
        

        