class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[-1]

        nums = deque(nums)

        val = 0
        while nums:
            val = val + nums.popleft()

            m = max(m,val)
            
            if val < 0:
                val = 0
            
        return m
        #[2,-3,4,-2,2,1,-1,4]

