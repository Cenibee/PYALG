class Solution:
    def isHappy(self, n: int) -> bool:
      history = set()
      while True:
          history.add(n)
          n = sum([int(s) ** 2 for s in str(n)])
          if n in history:
            break
      return n == 1