from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums 의 요소중 두 개를 택하여 더했을 때 target이 되는 두 숫자의 인덱스를 반환하라
            - 겹치는 숫자는 없다.
            - 정답은 반드시 하나만 존재한다.
            - 정답의 순서는 상관없다.
            - 2 <= nums.length <= 103
            -109 <= nums[i] <= 109
            -109 <= target <= 109
        way1
            - greedy
        '''
        for i in range(len(nums)):
            for o in range(i + 1, len(nums)):
                if nums[i] + nums[o] == target:
                    return [i, o]

sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))
print(sol.twoSum(nums = [3,2,4], target = 6))
print(sol.twoSum(nums = [3,3], target = 6))