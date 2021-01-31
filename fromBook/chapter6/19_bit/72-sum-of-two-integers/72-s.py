class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        if a == 0: return b
        elif b & mask == 0:
            if b > 0: # b > 0 means overflow
                return (a & mask)
            else:
                return a
        print(a, b)
        return self.getSum(a^b, (a&b)<<1)

sol = Solution()
print(sol.getSum(123, -97))

# 요거 안됨