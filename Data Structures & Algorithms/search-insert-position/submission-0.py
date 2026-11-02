class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i,val in enumerate(nums): 
            if val ==target :
                return i 
            if val>target:
                return i
        return len(nums)