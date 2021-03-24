# Definition for a binary tree node.
from typing import Deque, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = get_height(node.left)
            if left_height == -1: return -1

            right_height = get_height(node.right)
            if right_height == -1 or\
                abs(left_height - right_height) > 1:
                    return -1
            return max(right_height, left_height) + 1

        return get_height(root) != -1

sol = Solution()

print(sol.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, right=TreeNode(3, right=TreeNode(4))))))