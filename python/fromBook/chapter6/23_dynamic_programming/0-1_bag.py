def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo)):
        pack.append([])
        for c in range(capacity - 1):
            # 첫 번째 화물 or 첫 번째 기준인 경우 0
            if i == 0 or c == 0:
                pack[i].append(0)
            # 지금까지 탐색한 화물 조합으로 최대 가격을 구한당
            elif cargo[i - 1][1] < c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])

    return pack[-1][-1]