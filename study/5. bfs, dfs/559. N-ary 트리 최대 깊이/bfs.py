from typing import Deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0

        ans = 0
        q = Deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.children:
                    q += node.children
            ans += 1

        return ans