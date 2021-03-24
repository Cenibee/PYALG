from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
      nums = [start + 2 * i for i in range(n)]
      return reduce(lambda i, j: int(i) ^ int(j), nums)