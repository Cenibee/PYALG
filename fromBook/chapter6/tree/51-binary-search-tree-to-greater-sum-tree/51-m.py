# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # 현재 노드를 root로 하는 서브트리 노드의 모든 val의 합
        def sub_func(node: TreeNode, upper_sum: int) -> int:
            if node.right: upper_sum = sub_func(node.right, upper_sum)
            node.val = upper_sum = upper_sum + node.val
            if node.left: upper_sum = sub_func(node.left, node.val)
            return upper_sum

        sub_func(root, 0)
        return root

