class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # you start at 1 
        sol = []
        def permutate(current, remaining):
            if not remaining: 
                sol.append(current)

            for i in range(len(remaining)):
                permutate(current+[remaining[i]]  ,remaining[:i]+ remaining[i+1:])

        

        permutate([],nums)
        return sol 