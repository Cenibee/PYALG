class Solution:
    # 하향식 접근
    fib_res = dict()
    def fib(self, n: int) -> int:
        if not n: return 0
        elif n == 1: return 1

        if n not in self.fib_res:
            self.fib_res[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.fib_res[n]