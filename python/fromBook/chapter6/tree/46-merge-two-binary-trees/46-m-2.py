# Definition for a binary tree node.
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.val += t2.val

        return t1


def fulfil_tree(l: list) -> TreeNode:
    root = TreeNode(l[0])
    q = Deque([root])
    i = 1
    while q:
        node = q.popleft()
        if len(l) > i and l[i]:
            node.left = TreeNode(l[i])
            q.append(node.left)
        if len(l) > i+1 and l[i]:
            node.right = TreeNode(l[i + 1])
            q.append(node.right)
        else:
            break
        i += 2
    return root

sol = Solution()
print(sol.mergeTrees(fulfil_tree([1,3,2,5]),fulfil_tree([2,1,3,None,4,None,7])))