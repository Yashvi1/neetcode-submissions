class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        profit = 0
        for price in prices:
            cheapest = min(cheapest, price)
            today_profit = price - cheapest
            profit = max(profit, price-cheapest)
        return profit
            

        