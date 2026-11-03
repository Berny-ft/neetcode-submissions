class Solution:
    def jump(self, nums: List[int]) -> int:
        # we are now looking for the minimum number of jumps 
        
        jumps = 0
        lo, hi = 0, 0  

        while hi < len(nums) - 1:
            new_hi = hi
            for i in range(lo, hi + 1):
                new_hi = max(new_hi, i + nums[i])
            lo = hi + 1
            hi = new_hi
            jumps += 1

        return jumps


        

        
        