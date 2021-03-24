from typing import DefaultDict


class Solution:
    dp = DefaultDict(int)
    def fib(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[n] = self.dp[n - 1] + self.dp[n - 2]
        return self.dp[n]