import heapq
from typing import DefaultDict

class Solution:
    def frequencySort(self, s: str) -> str:
        m = DefaultDict(int)

        for ch in s: m[ch] += 1

        priority_q = []
        for key  in m.keys():
            heapq.heappush(priority_q, (-1 * m[key], key))

        ans = []
        while priority_q:
            count, key = heapq.heappop(priority_q)
            ans.append(key * (-1 * count))
        return ''.join(ans)

sol = Solution()
print(sol.frequencySort("tree"))