class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        for i in range(1,len(nums)):
            left.append( left[i-1] * nums[i] )


        
        right = [nums[len(nums)-1]]
        n = len(nums)
        for i in range( n-2, -1,-1):
            right.append( right[-1] * nums[i])
        right = right[::-1]

 
        return  [right[1]] +  [ left[i-1]* right[i+1] for i in range(n) if i not in [0,n-1]] +  [left[-2]]

        

