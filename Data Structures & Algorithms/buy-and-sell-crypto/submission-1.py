class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0 

        """
        wha tis the strategy 
        the seasy way is for each value look in the future and find the max  so i'll do htat quickly now

        """
        for i,val in enumerate(prices):
            for j in prices[i:len(prices)]:
                if j - val  > profit:
                    profit = j - val
                    print(j,i)

        return profit
        