class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = prices[0]

        for i in range(len(prices)): 
        
            if prices[i] > sell: 
                sell = prices[i]
        
            if prices[i] < buy: 
                buy = prices[i]
                sell = prices[i]
        
            profit = max(profit, sell - buy)

        return profit

