from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            tester = target - n
            if tester in nums_map:
                return [i, nums_map[tester]]
            nums_map[n] = i

sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))
print(sol.twoSum(nums = [3,2,4], target = 6))
print(sol.twoSum(nums = [3,3], target = 6))