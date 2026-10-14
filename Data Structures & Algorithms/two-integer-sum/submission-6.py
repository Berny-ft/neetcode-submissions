class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        table = {}
        for i,val  in enumerate(nums):
            if target-val in table:
                return [ table[target-val], i]
            else:
                table[val] = i



        