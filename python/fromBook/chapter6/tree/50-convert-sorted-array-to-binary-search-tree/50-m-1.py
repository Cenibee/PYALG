# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        def divide(fr: int, to: int) -> TreeNode:
            if fr == to:
                return TreeNode(nums[fr])
            elif fr + 1 == to:
                return TreeNode(nums[to], TreeNode(nums[fr]))

            center = (to + fr) // 2
            return TreeNode(nums[center],
                divide(fr, center - 1),
                divide(center + 1, to))

        return divide(0, len(nums) - 1)

sol = Solution()
sol.sortedArrayToBST([0,1,2,3,4,5,6,7,8,9,10,15,17])