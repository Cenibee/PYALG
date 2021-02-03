from collections import defaultdict, deque
from typing import DefaultDict
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_accessor = defaultdict(int)
        for ch in t: t_accessor[ch] += 1
        check = set()

        q = deque()
        pos = (0, 100000)
        for i, ch in enumerate(s):
            if ch not in t_accessor: continue

            q.append((i, ch))
            t_accessor[ch] -= 1
            if not t_accessor[ch]: check.add(ch)

            if q[0][1] == q[-1][1]:
                while t_accessor[q[0][1]] < 0:
                    t_accessor[q.popleft()[1]] += 1

            if len(check) == len(t_accessor) and\
                    q[-1][0] - q[0][0] < pos[1] - pos[0]:
                pos = (q[0][0], q[-1][0])

        if pos[1] > len(s): return ''
        return s[pos[0]: pos[1] + 1]

sol = Solution()
sol.minWindow("bdab","ab")