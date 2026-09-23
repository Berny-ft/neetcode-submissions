class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0

        right = len(nums) - 1

        while left <= right : # at the end right will have the righ tindex
            mid = left + (right - left) //2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # mid does't have the value so we msut go apst it 
                left = mid + 1
            else:
                right = mid -1
            
        
        return -1
        