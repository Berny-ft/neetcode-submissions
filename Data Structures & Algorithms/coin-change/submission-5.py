class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ''' done through dp find all the coins that are doable up to amount 
        if an amount needs to be reached we look theroughth elikst of couns avaialbe we count a count of ekayc type and then we ask look for how many coins to make the remeing which will aredy be in the dp array or not doiable  if 

        so what is the algorihtm
        create a dp array of size amount + 1 since 0 is doable 

        for each amount we check in teh coins (for loop):
            we keep track a min 
            fo every iteration we check how any coins ti tooks if it lesser than teh min we change hte min to that value with a min initallized to infinite 
            for each coin we will check 
            if if amount - coin in dp return 1 + d[coin-amoint]
            then teh number of coin is compared ot the min and and we only kepe the min coin count

        in the end re return d[ampunt+1] if itis less then ifnity of not we return -1


        '''

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for value in range(1,amount+1):

            minn = float('inf')
            for coin in coins:
                if (value - coin) >= 0 :
                    count = 1 + dp[value-coin]
                    minn = min(minn, count)
            dp[value] = minn
            
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1


        