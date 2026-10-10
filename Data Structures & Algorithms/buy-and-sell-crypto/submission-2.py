class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0 

        """
        wha tis the strategy 
        the seasy way is for each value look in the future and find the max  so i'll do htat quickly now

        """
        """
        for i,val in enumerate(prices):
            for j in prices[i:len(prices)]:
                if j - val  > profit:
                    profit = j - val
                    print(j,i)

        return profit

        """ # that is done in 02

        ''' we want to do it in one pass meaning 
        we nee da stack probalby 


        '''
        profit = 0
        min_yet = prices[0]
        for i in prices[1:]:
            profit =   max(profit, i - min_yet)
            if i < min_yet:
                min_yet = i
        return profit
            
        