from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(left: int, right: int, find:int) -> int:
            while left < right:
                mid = left + (right - left) // 2
                if numbers[mid] == find:
                    return mid
                elif numbers[mid] < find:
                    left = mid + 1
                else:
                    right = mid
            return -1

        maximum = len(numbers)
        for idx, num in enumerate(numbers):
            if num + numbers[0] > target:
                maximum = idx + 1

        for i in range(maximum - 1):
            res = binary_search(i + 1, maximum, target - numbers[i])
            if res != -1:
                return [i + 1, res + 1]

sol = Solution()
# sol.twoSum([2,7,11,15],9)
sol.twoSum([2,3,4],6)