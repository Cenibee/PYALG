from typing import List, DefaultDict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = DefaultDict(int)
        for num in nums:
            if num in m: m[num] += 1
            else: m[num] = 1
        
        return max(m, key=lambda x: m[x])
