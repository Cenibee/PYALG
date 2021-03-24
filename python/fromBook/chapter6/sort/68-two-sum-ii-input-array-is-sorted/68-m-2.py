from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1

        while right < len(numbers) - 1 and numbers[left] + numbers[right] < target: right += 1
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]

        while left < right:
            if numbers[left] + numbers[right] == target: return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return []

sol = Solution()
sol.twoSum([0,0,3,4],0)