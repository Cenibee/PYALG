from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        one, two = 0,0,0
        idx = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if num == 0:
                nums[idx] = 0
                idx += 1
            elif num == 1: one += 1
            else: two += 1

        for i in range(idx, len(nums)):
            if one:
                nums[i] = 1
                one -= 1
            elif two:
                nums[i] = 2
                two -= 1
