from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = set()
        for num in nums1:
            m.add(num)

        ans = []
        for num in nums2:
            if num in m:
                ans.append(num)
                m.remove(num)

        return ans