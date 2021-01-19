class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val < low:
                    stack.append(node.right)
                if node.val > high:
                    stack.append(node.left)
                if low <= node.val <= high:
                    sum += node.val
        return sum