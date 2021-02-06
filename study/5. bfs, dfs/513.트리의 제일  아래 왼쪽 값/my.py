from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # BFS 대상을 저장할 큐
        q = Deque([root])
        ans = root.val

        # BFS 순회문
        while q:
            # 선입된 값을 가져온다.
            node = q.popleft()

            # val 을 ans 로 지정한다.
            ans = node.val

            # right - left 순으로 입력한다.
            # left가 후입 됐기 때문에, 최종 ans 는 해당 레벨의 제일 왼쪽 값을 갖는다.
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)

        return ans
