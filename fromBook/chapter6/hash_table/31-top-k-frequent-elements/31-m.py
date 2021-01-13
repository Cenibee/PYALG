from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        return [num[0] for num in counter]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3,3,3,3], k = 2))