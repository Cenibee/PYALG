import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = ~sys.maxsize
        last_calc = 0

        for i in range(len(nums)):
            last_calc = max(last_calc + nums[i], nums[i])
            m = max(m, last_calc)
        return m