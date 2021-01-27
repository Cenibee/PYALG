from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        head = mid = 0
        tail = len(nums) - 1

        while mid <= tail:
            if nums[mid] == 0:
                nums[head], nums[mid] = nums[mid], nums[head]
                head += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[tail] = nums[tail], nums[mid]
                tail -= 1