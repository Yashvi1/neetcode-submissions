class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        profit = 0
        for price in prices:
            if cheapest > price:
                cheapest = price
            today_profit = price - cheapest
            if today_profit > profit:
                profit = today_profit
        return profit
            

        