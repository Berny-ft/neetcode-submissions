class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # skip duplicates 
                continue
            l,r = 1+i, len(nums)-1  # setting the left and righ tpointers: wodln't this implementation skip the first elemtn at i = 0 why are we increming the first index

            # post increment left means left is not equal to i by default. therefore we do a two pointer imlementaiton where we at each point select an element and then from left to right our left and right check go until they 
            while l < r:
                s = nums[i] + nums[l] + nums[r] # this implementation guaranteese that there won't be duplicates so atlow so to remove a lot of edges cases that woudl have been manually implemented if the array wasn't sorted initially 
                if s == 0: # we got a set 
                    res.append([nums[l],nums[r],nums[i]])
                    # in this case we must move buth in
                    l += 1
                    # post increment background check 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < 0 : # we are under the limit therefore we increment the left 
                    l += 1
                    # post increment background check 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    r -= 1

        
        return res
        