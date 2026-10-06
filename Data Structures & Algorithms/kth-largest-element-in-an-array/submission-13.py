class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ''' so the startelgy here is pretty simple 
        you creata heap in which you push k lements necesary the top elemtn is going to the min and itis going ot be the keth largest at the same time. now if you push an additional ement it may be larger than the current kth largest but lesser than all other values this is fine that mean th epreviosu min has ot removed and the current just added value is the new kth largest 

        esseentailly if you makve a min heap containing only k items neceessary the smallest oneis the kth largest one . how do you mke sure it says that way . well you make sure that the heap stays the same size. meaning at eahc addition you have to remove another elemetn . so if i adadd all ements inmy heap then i remove all the lemetns leaving only k well the remaing k elemtns wwill necearrily bhe the largest elemtns and the top will be the kth largest. but that woudl be 2 passes we can do it in one pass but makign sure we have at most k alement eavery time wha th doesis is that puspop.. theres a gap in my understanding a bit here 

        '''

        import heapq

        h = []
        for i in range(k):
            heapq.heappush(h,nums[i])

        for i in range(k,len(nums)):

            heapq.heappushpop(h,nums[i])

        return heapq.heappop(h)

        '''vnums=[-1,2,0]
k=1''' #this edge case kepth fail'''
        