class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for sell in prices:
            if sell > min_buy:
                profit = sell - min_buy
                if profit > max_profit:
                    max_profit = profit
            else:
                min_buy = sell
        return max_profit
