# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node

        p = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:p + 1], inorder[0:p])
        node.right = self.buildTree(preorder[p + 1:], inorder[p + 1:])
        return node

sol = Solution()
sol.buildTree([7,3,1,0,2,5,4,6],[0,1,2,3,4,5,6,7])