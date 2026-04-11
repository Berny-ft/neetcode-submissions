class Solution:
    def rob(self, nums: List[int]) -> int:

        # kinda of a of a sketchy solution in the way its written but I think its just right 
        if len(nums) == 1:
            return nums[0]
        
        rob1 = 0
        rob2 = 0

        for i in nums[1:]:
            temp = max(rob1+i, rob2)
            rob1 = rob2
            rob2 = temp
        max1 = rob2
        rob1 = 0
        rob2 = 0

        for i in nums[:-1]:
            temp = max(rob1+i, rob2)
            rob1 = rob2
            rob2 = temp

        max2 = rob2
        return max(max1,max2)