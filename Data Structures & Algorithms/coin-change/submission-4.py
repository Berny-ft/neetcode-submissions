class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount + 1)
        coins = set(coins)

        # at eahc amoutn i say can i make it for all coins ive got if the coin is too big we skip 
        # if the coin is too small we  we ake a tentaive coin and we check how many coins to make the rest if the rest doenst' exist we leaeve it ti info it ny if it rest exist we a add one ot it and set that vlaue if we have the exact amount of coins we return 1 .  now woudl this be the minima way to do it ? think so 

        for i in range(amount + 1): # we need to cover teh amount itself 
            if i in coins:
                dp[i] = 1
                continue
            
            m = float('inf')
            for coin in coins:
                if i > coin :
                    diff = i - coin # this will be in the dp array
                    m = min(m, 1 + dp[diff])
            
            if m != float('inf'):
                dp[i] = m
            
        return dp[amount] if dp[amount] != float('inf') else -1

        