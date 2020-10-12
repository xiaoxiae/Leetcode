class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        min_i_value = float("+inf")

        for i in range(len(prices)):
            if prices[i] < min_i_value:
                min_i_value = prices[i]
            else:
                if prices[i] - min_i_value > max_profit:
                    max_profit = prices[i] - min_i_value

        return max_profit
