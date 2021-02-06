# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # root 가 None 이면 root 반환
        if not root: return root

        # 정답을 저장할 ans와 현재까지 경로를 저장할 path
        ans = []
        path = []

        # DFS 를 재귀 함수로 구현
        def dfs(node: TreeNode):
            # 일단 우선 path 에 val을 put()
            path.append(str(node.val))

            # 리프 노드라면, ans에 현재까지 경로를 추가하고 pop()
            if not node.left and not node.right:
                ans.append('->'.join(path))
                path.pop()
                return

            # DFS의 다음 재귀
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)

            # 현 경로 탐색이 끝났다면 pop()
            path.pop()

        # root부터 DFS를 시작
        dfs(root)
        return ans