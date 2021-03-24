from typing import Counter, List
import heapq

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)
        ans = 0

        while g and s:
            child = heapq.heappop(g)
            cookie = heapq.heappop(s)

            while s and child > cookie:
                cookie = heapq.heappop(s)
            if child <= cookie:
                ans += 1

        return ans
