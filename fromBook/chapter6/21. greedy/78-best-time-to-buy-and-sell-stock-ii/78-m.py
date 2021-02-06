from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_from = [0] * (len(prices) + 1)
        for i in range(len(prices) - 2, -1, -1):
            max_profit_from[i] = max_profit_from[i + 1]
            if prices[i] >= prices[i + 1]:
                continue
            for o in range(i + 1, len(prices)):
                profit = max_profit_from[o + 1]
                if prices[i] < prices[o]:
                    profit += prices[o] - prices[i]
                if max_profit_from[i] < profit:
                    max_profit_from[i] = profit
        return max_profit_from[0]

sol = Solution()
sol.maxProfit([7,1,5,3,6,4])