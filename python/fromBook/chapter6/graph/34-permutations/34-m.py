from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        prev_result = self.permute(nums[1:])
        result = []
        current_num = nums[0]
        for current_array in prev_result:
            for o in range(0, len(current_array) + 1):
                temp = current_array[:]
                temp.insert(o, current_num)
                result.append(temp)

        return result

sol = Solution()
print(sol.permute([1,2,3]))
a = []