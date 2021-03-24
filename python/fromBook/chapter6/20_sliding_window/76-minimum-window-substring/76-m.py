from collections import defaultdict, deque
from typing import DefaultDict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_accessor = defaultdict(int)
        for ch in t: t_accessor[ch] += 1
        check = set()
        f = 0
        while f < len(s) and s[f] not in t_accessor:
            f += 1
        if f >= len(s): return ''

        q = deque()
        pos = (0, float('inf'))
        for i in range(f, len(s)):
            if s[i] not in t_accessor: continue

            q.append((i, s[i]))
            t_accessor[s[i]] -= 1
            if not t_accessor[s[i]]:
                check.add(s[i])

            # 큐의 맨 앞, 맨 뒤 문자가 같다면 reduce를 진행한다.
            if q[0][1] == q[-1][1]:
                while t_accessor[q[0][1]] < 0:
                    t_accessor[q.popleft()[1]] += 1

            # 현재 q 의 원소 종류 개수가 t의 문자 종류 개수와 같고
            # pos 간격이 더 좁다면
            if len(check) == len(t_accessor) and\
                    q[-1][0] - q[0][0] < pos[1] - pos[0]:
                # pos 업데이트
                pos = (q[0][0], q[-1][0])
        if pos[1] > len(s):
            return ''
        return s[pos[0]: pos[1] + 1]

sol = Solution()
sol.minWindow("bdab","ab")