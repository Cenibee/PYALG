class Solution:
    def isHappy(self, n: int) -> bool:
        result_m = {}

        def calculate(num:int) -> int:
            if num in result_m:
                return -1
            temp = num
            res = 0
            while temp:
                temp, mod = divmod(temp, 10)
                res += mod ** 2
            result_m[num] = res
            return res

        while True:
            n = calculate(n)
            if n == -1:
                return False
            if n == 1:
                return True

sol = Solution()
sol.isHappy(19)

# 리스트 컴프리헨션은 빠르다
# 타입 캐스팅이 생각만큼 느리지 않은것 같다.