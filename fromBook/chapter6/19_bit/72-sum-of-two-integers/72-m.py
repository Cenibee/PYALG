class Solution:
    def getSum(self, a: int, b: int) -> int:
        # if a == b * -1: return 0
        # while b != 0:
        #     a, b = a ^ b, (a & b) << 1
        a = bin(a)
        b = bin(b)

        c = int(a) ^ int(b)
        return a


sol = Solution()
sol.getSum(-14, 16)

