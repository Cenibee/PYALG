from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        while g and s:
            child = g.pop()
            if s[-1] >= child:
                s.pop()
                ans += 1
        return ans