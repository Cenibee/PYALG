from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) >= 2: nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])

        return nums[-1]