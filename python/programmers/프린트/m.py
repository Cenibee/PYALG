import bisect
from typing import DefaultDict

def solution(priorities, location):
    m = DefaultDict(list)

    # priority: [i1, i2, ...] 형식으로 변환
    for i, p in enumerate(priorities):
        m[p].append(i)

    count = 0
    # 역순으로 정렬된 키를 순회
    key = sorted(m.keys(), reverse=True)

    # 이전 숫자가 종료된 인덱스 처음 순회에서 타겟 priority 면 0으로 설정해서 바로 끝나게
    last_end = len(priorities) - 1 if key[0] != priorities[location] else 0

    for i in key:
        # 타겟 priority 가 아니라면 카운트 하고 마지막 인덱스 저장
        if i > priorities[location]:
            last_end = m[i][bisect.bisect(m[i], last_end) - 1]
            count += len(m[i])

        # 타겟 priority 라면 이전 마지막 인덱스로부터 몇 번째에 있는지 계산해서 출력
        elif i == priorities[location]:
            location = bisect.bisect_left(m[i], location)
            last_end = bisect.bisect_left(m[i], last_end)
            if location >= last_end:
                return count + (location - last_end) + 1
            else:
                return count + len(m[i]) - last_end + location + 1

# 내가 푼게 시간복잡도는 상당히 괜찮은 것 같다.
# 다른 사람 참고에서 얻어갈 것 any([컴프리헨션 형식의 반복문]) -> Bool