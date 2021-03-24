from typing import DefaultDict, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = DefaultDict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num