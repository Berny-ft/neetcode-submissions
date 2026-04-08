class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            if not remaining : 
                return 1
            if remaining < 0 :
                return 0

            memo[remaining] = dfs(remaining -1) + dfs(remaining-2)
            return memo[remaining]

        return dfs(n)