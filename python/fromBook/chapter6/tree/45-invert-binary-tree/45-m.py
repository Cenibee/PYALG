# Definition for a binary tree node.
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = Deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return root