def solution(progresses, speeds):
    for i in range(len(progresses)):
        d, m = divmod(100 - progresses[i], speeds[i])
        progresses[i] = d + (1 if m else 0)

    answer = []
    mark = 0
    for i in range(len(progresses)):
        if mark != i and progresses[mark] < progresses[i]:
            answer.append(i - mark)
            mark = i

    answer.append(len(progresses) - mark)
    return answer

'''
다른 사람 풀이 보고 배운 부분

1.
divmod를 사용해서 mod 0 or not 을 판별할때
**음수로 변환하여 // 를 수행** 하면 풀이 시간을 절약할 수 있다.

2.
반복문 똑같으면 그냥 합쳐두댐 if 랑 똑같은거자낭!
'''