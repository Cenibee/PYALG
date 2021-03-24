from typing import Counter, List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,3,3,3], k = 2))