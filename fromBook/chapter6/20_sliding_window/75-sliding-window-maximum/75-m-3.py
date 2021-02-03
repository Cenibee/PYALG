from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, ans = deque(), []

        for i in range(len(nums)):
            if i >= k:
                ans.append(q[0])
                if nums[i - k] == q[0]: q.popleft()

            while q and nums[i] > q[-1]: q.pop()
            q.append(nums[i])

        ans.append(q[0])
        return ans

# conclusion
# 1. deque 사용할 땐 스택과 동일한 알고리즘을 처리할 수 있다는걸 생각하자
#     - 물론 큐도 마찬가지