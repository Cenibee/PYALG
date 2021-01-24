from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def template(num: str) -> str:
            return num + (num[-1] * (10 - len(num)))

        nums = [str(x) for x in nums]
        nums.sort(reverse=True, key=template)
        return ''.join(nums)

sol = Solution()
print(sol.largestNumber([34, 30, 9, 5, 3]))
print(sol.largestNumber([34, 30, 32, 333, 387]))
print(sol.largestNumber([34323,3432]))

def template(num: str) -> str:
    return num + (num[-1] * (10 - len(num)))

print(template(str(34323)))
print(template(str(3432)))