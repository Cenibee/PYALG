from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        pre_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(pre_elements[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                pre_elements.append(e)
                dfs(next_elements)
                pre_elements.pop()

        dfs(nums)
        return results