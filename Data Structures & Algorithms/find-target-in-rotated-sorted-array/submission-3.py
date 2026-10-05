class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # this is a remainder problem 
        #  you shoudl just add the number of rations to the startet indice and due module n to it so that you get the nw psotion 
        # the algo for 

        # how do you detemrine if a value has been 

        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: # the left half is storted
                if  nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: 
                    left = mid + 1 

            else:##the right hafl is storsorteded
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1

        