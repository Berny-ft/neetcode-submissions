class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol = []
        end = len(nums)

        def backtrack(current,index):
            # you decide if you add the current elemtn or not 

            if index == end:
                sol.append(current)
                return 
            
            backtrack(current, index+ 1)
            backtrack(current + [nums[index]], index+1)


        backtrack([],0)

        return sol
        