class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maximum = nums[0]

        curr_max = maximum
        for i in range(1,len(nums)):
            val = nums[i]

            if val > curr_max + val:
                curr_max = val
            else:
                curr_max += val
            
            maximum = max(curr_max, maximum)
        
        return maximum
