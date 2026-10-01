class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2:
            return max(nums)



        left = nums[0]
        right = max(left, nums[1])


        for i in range(2,n):
            # you've got 2 choises here 
            # rob or don't rob 
            value = nums[i]
            temp = right

            right = max( left + value, right)
            left  = temp
        print(right)
        return right

        