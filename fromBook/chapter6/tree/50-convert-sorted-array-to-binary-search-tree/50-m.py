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
        center = len(nums) // 2
        return TreeNode(nums[center],
            self.sortedArrayToBST(nums[:center]),
            self.sortedArrayToBST(nums[center + 1:]))