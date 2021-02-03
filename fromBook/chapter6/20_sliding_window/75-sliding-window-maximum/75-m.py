from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p1 = 0
        p2 = k

        ans = []
        while p2 <= len(nums):
            ans.append(max(nums[p1:p2]))
            p1 += 1
            p2 += 1
        return ans

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

# 시간 초과