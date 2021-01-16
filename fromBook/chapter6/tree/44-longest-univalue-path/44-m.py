# Definition for a binary tree node.
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        주어진 이진 트리 root 에 대해 같은 값을 가지는 노드간 거리가 가장 긴 길이를 반환하라.
        길이는 두 노드 사이의 엣지 개수를 나타낸다.
        """
        if not root:
            return 0
        def dfs(node: TreeNode) -> int:
            left_path_len = 0
            right_path_len = 0

            if node.left:
                if node.left.val == node.val:
                    left_path_len += dfs(node.left) + 1
                else:
                    dfs(node.left)

            if node.right:
                if node.right.val == node.val:
                    right_path_len += dfs(node.right) + 1
                else:
                    dfs(node.right)

            self.result = max(left_path_len + right_path_len, self.result)

            return max(left_path_len, right_path_len)

        latest = dfs(root)
        return max(self.result, latest)


sol = Solution()

def fulfil_tree(l: list) -> TreeNode:
    root = TreeNode(l[0])
    q = Deque([root])
    i = 1
    while q:
        node = q.popleft()
        if len(l) > i:
            node.left = TreeNode(l[i])
            q.append(node.left)
        if len(l) > i+1:
            node.right = TreeNode(l[i + 1])
            q.append(node.right)
        else:
            break
        i += 2
    return root

print(sol.longestUnivaluePath(fulfil_tree([1, 4,5,4,4,5])))
