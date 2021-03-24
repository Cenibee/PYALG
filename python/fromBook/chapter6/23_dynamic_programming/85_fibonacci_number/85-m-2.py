class Solution:
    # 상향식 접근
    def fib(self, n: int) -> int:
        if n < 2: return n
        fbn = [0, 1]

        for i in range(1, n):
            fbn.append(fbn[i] + fbn[i - 1])

        return fbn[-1]