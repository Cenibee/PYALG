from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        배열의 i 번 쨰 요소는 i 날에 주어진 주식의 가격이다.
        한 번 사고 한 번 팔아 최대 이익을 낼 수 있는 알고리즘을 구하라
        '''
        # 길이가 2보다 작으면 무조건 0
        if len(prices) < 2:
            return 0

        buy = prices[0]
        sell, max_profit = 0, 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                max_profit = max(max_profit, sell - buy)
                buy = prices[i]
                sell = 0
            elif sell < prices[i]:
                sell = prices[i]

        return max(max_profit, sell - buy)



sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([1, 2]))