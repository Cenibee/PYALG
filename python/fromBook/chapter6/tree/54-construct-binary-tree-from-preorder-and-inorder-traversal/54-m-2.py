# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dnc(pre_from: int, pre_to: int,\
            in_from: int, in_to: int) -> TreeNode:
                if pre_from == pre_to:
                    return None
                node = TreeNode(preorder[pre_from])
                if pre_from + 1 == pre_to:
                    return node

                p = inorder.index(preorder[pre_from], in_from) - in_from

                node.left = dnc(pre_from + 1, pre_from + p + 1,
                        in_from, in_from + p)
                node.right = dnc(pre_from + p + 1, pre_to,
                         in_from + p + 1, in_to)
                return node
        return dnc(0, len(preorder), 0, len(inorder))

sol = Solution()
sol.buildTree([7,3,1,0,2,5,4,6],[0,1,2,3,4,5,6,7])