from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum

sol = Solution()
print(sol.arrayPairSum([1,4,3,2]))
print(sol.arrayPairSum([6,2,6,5,1,2]))