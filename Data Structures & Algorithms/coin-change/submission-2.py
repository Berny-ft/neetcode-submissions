class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        dp = [float("inf") for i in range(amount+1)]
        
        dp[0] = 0

        for i in coins:
            if i <= amount:
                dp[i] = 1
        
        for i in range(min(coins),len(dp),1):
            for coin in (coins):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]
                


