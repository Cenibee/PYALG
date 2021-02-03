import sys
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        max_idx = -1
        max_sliding = ~sys.maxsize
        for _ in range(0, k):
            max_sliding = max(nums[right], max_sliding)
            if max_sliding == nums[right]:
                max_idx = right
            right += 1

        ans = [max_sliding]
        while right < len(nums):
            if nums[right] >= max_sliding:
                max_sliding = nums[right]
                max_idx = right
            right += 1

            if nums[left] == max_sliding and left == max_idx:
                max_idx = left + 1
                max_sliding = nums[max_idx]
                for i in range(left + 2, right):
                    max_sliding = max(nums[i], max_sliding)
                    if max_sliding == nums[i]:
                        max_idx = i
            left += 1
            ans.append(max_sliding)
        return ans