def solution(progresses, speeds):
    answer = []
    mark = 0
    for i in range(len(progresses)):
        progresses[i] = (progresses[i] - 100) // speeds[i]

        if mark != i and progresses[mark] > progresses[i]:
            answer.append(i - mark)
            mark = i

    answer.append(len(progresses) - mark)
    return answer