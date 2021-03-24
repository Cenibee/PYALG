def solution(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

# ... 기준이 되는 수를 이용해 여러 연산을 트라이 해보는게 큰 의미가 있겠군