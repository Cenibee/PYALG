'''
순환로에 n 개의 주유소가 있고, 각각의 주유소에는 gas[i] 양 만큼 가스가 있다.
무제한의 가스탱크가 잇는 차를 운전한다.
i -> i + 1 로 이동시에 필요한 가스의 양은 cost[i] 이다.
가스가 빈 상태로 임의의 주유소에서 출발한다.
gas 와 cost 가 주어졌을 때, 전체를 순환가능한 시작점을 반환하라.
불가능 하다면 -1을 반환하고, 정답은 반드시 하나라고 보장한다.
'''

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = -1

        # cost: i -> i+1 가고 남는 가스의 양 (cost[i] = gas[i] - cost[i])
        for i in range(n):
            cost[i] = gas[i] - cost[i]

            # 0 이상이라면 시작점 후보에 add 한다.
            if cost[i] >= 0:
                start = i

        if sum(cost) < 0: return -1

        end = start
        size = 1
        remain = cost[start]

        # 시작한 점에서 부터 앞뒤로 확장해 나간다.
        while size < n:
            if remain >= 0:
                end = (end + 1) % n
                remain += cost[end]
            else:
                start = (start - 1) % n
                remain += cost[start]
            size += 1

        if remain >= 0: return start
        else: return -1
