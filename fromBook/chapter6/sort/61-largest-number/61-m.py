from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def template(str1: str, str2: str) -> int:
            if str1 + str2 >= str2 + str1:
                return -1
            else:
                return 1

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(template))
        if nums[0][0] != '0': return ''.join(nums)
        else: return '0'

sol = Solution()
print(sol.largestNumber([34, 30, 9, 5, 3]))
print(sol.largestNumber([34, 30, 32, 333, 387]))
print(sol.largestNumber([34323,3432]))

def template(num: str) -> str:
    return num + (num[-1] * (10 - len(num)))

print(template(str(34323)))
print(template(str(3432)))

## 모르겠다 ㅈㅈ ㅠㅠㅠ