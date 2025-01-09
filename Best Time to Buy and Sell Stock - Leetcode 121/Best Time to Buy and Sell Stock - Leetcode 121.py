class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        lowest_price = prices[0]
        highest_price = prices[0]

        for price in range(len(prices)):
            if (prices[price] < lowest_price):
                lowest_price = prices[price]

            current_price = prices[price] - lowest_price
            if (current_price > max_profit):
                max_profit = current_price
        
        return max_profit