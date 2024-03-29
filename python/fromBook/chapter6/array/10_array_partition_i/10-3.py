from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

sol = Solution()
print(sol.arrayPairSum([1,4,3,2]))
print(sol.arrayPairSum([6,2,6,5,1,2]))