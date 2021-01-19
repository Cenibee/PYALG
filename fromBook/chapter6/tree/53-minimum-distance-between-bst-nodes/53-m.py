import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    min_diff = sys.maxsize
    last_num = ~sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        '''
        어떤 두 수간 차의 최소값을 구하라.
            - 일단 전체 탐색을 해야할 것 같다.
                - 단, 최솟값인 1을 구했을 때는 바로 리턴해도 될듯
                - 왜냐면 연속되는 어떤 두 수를 특정할 수 없으니까.
            - 순서를 봐야하니 DFS로 구현하고, 전 - 중 - 후
        '''
        if not root:
            return 0

        if root.left: self.minDiffInBST(root.left)

        self.min_diff = min(self.min_diff, root.val - self.last_num)
        self.last_num = root.val

        if root.right: self.minDiffInBST(root.right)

        return self.min_diff