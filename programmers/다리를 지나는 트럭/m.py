from typing import Deque

def solution(bridge_length, weight, truck_weights):
    # 앞에 부터 없애기 위해 Deque 사용
    q = Deque()
    truck_weights = Deque(truck_weights)
    time = cur_weight = 0

    # 남은 트럭이 있는 동안
    while truck_weights:

        # 다음 트럭 출발 가능하면 출발
        if cur_weight + truck_weights[0] <= weight:
            chain_count = 0 if not q or q[-1][0] > 0 else q[-1][0] - 1
            q.append([chain_count, truck_weights.popleft()])
            cur_weight += q[-1][1]

        # 다음 트럭이 출발 불가능하면
        else:
            # 제일 앞 트럭 나가고
            pos, w = q.popleft()
            cur_weight -= w

            update = bridge_length - pos
            time += update
            # 이동한 거리만큼 다리위 트럭 업데이트
            for i in range(len(q)):
                q[i][0] += update

    return time + (bridge_length - q[-1][0]) + 1