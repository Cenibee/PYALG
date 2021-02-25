# memoization

from typing import DefaultDict

class Solution:
    dp = DefaultDict(int)
    def fib(self, n: int) -> int:
        if n <= 1: return n
        elif self.dp[n]: return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]
