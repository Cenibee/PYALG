# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root: TreeNode) -> int:
            if not root:
                return 0

            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0
            self.max = max(self.max, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.max

