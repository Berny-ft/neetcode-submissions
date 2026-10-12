class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}
        for i,val in enumerate(nums):
            if val in m:
                return [ m[val], i]
            else:
                m[target-val] = i

        
        