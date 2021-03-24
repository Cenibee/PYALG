'''
초 단위 주식가격 배열 prices

'''
from typing import DefaultDict

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[j] < prices[i]:
                answer[i] = j - i + 1
                break
        if answer[i] == 0:
            answer[i] = len(prices) - 2
    return answer