class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        
        for i in range(1,len(nums)):
            left = nums[i-1]
            right = nums[i]

            if left == right:
                left *= 2
            
                right = 0
            
                nums[i-1] = left
                nums[i] = right

        
        print(nums)
        pos = 0
        arr = [0] * len(nums)
        for i in nums:
            print(i)
            if i != 0:
                arr[pos] = i
                pos += 1
        
        return arr

            



