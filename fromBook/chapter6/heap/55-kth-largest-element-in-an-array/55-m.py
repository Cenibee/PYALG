from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-1 * k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]