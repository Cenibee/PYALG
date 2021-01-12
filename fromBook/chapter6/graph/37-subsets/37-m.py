from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        def build_subset(num: int):
            for subset_index in range(0, len(results)):
                new_subset = results[subset_index][:]
                new_subset.insert(i, num)
                results.append(new_subset)

        for i in nums:
            build_subset(i)

        return results





sol = Solution()
print(sol.subsets( [1,2,3]))