class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        
        sol = []
        
        for i, val in enumerate(nums):
            
            if i > 0 and val == nums[i - 1]:   # fix 1: skip duplicate vals
                continue

            left = i + 1
            right = len(nums)-1
            
            complement = -val
            while left < right:
                if nums[left] + nums[right] > complement:
                    right -=1
                elif nums[left] + nums[right] < complement:
                    left += 1
                else:
                    sol.append([val, nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
                    right -=1
        
        return sol
                    
