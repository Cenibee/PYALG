from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (i, val) in enumerate(nums):
            tester = target - val

            if tester in nums[i + 1:]:
                return [i, nums[i + 1:].index(tester) + i + 1]

sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))
print(sol.twoSum(nums = [3,2,4], target = 6))
print(sol.twoSum(nums = [3,3], target = 6))