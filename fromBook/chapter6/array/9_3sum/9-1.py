from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0 :
                        results.append([nums[i], nums[j], nums[k]])
        return results

sol = Solution()
print(sol.threeSum([]))
print(sol.threeSum([0]))
print(sol.threeSum([1, 2]))
print(sol.threeSum([-1,0,1]))
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,0,0,0,0,0]))
print(sol.threeSum([-2,0,1,1,2]))
print(sol.threeSum([-2,-1,-1,0,1,2]))
print(sol.threeSum([-2,0,0,2,2]))
print(sol.threeSum([3,0,-2,-1,1,2]))