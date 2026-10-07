class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        sudocode
        dp[] * n 
        the best so far is value 0 staring at value 1
        max_state = dp[0]
        for i in range(1...)
            dp[i] = max(val, dp[i-1] + val)
            max_state = max(max_state, dp[i])

        return max_state

        '''


        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sub = dp[0]
        for i in range(1,len(nums)): # off by one since using enumrate
            dp[i] = max(nums[i], dp[i-1] + nums[i] )
            max_sub = max(max_sub, dp[i])

        return max_sub
