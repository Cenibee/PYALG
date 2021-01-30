from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i + k + 1] == expected:
                return [k + 1, i + k + 2]
