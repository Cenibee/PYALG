from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue, sum = Deque([root]), 0
        while queue:
            node = queue.popleft()
            if node:
                if node.val < low:
                    queue.append(node.right)
                if node.val > high:
                    queue.append(node.left)
                if low <= node.val <= high:
                    sum += node.val
        return sum