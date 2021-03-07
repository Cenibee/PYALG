def solution(n):
    criteria = 0
    inc = 1
    pos = -1
    while True:
        next_criteria = criteria + inc
        if criteria <= n < next_criteria:
            break
        criteria = next_criteria
        inc *= 3
        pos += 1

    n -= criteria
    ans = ['1'] * (pos + 1)

    while n and pos > -1:
        inc //= 3
        if n >= inc * 2:
            n -= inc * 2
            ans[pos] = '4'
        elif n >= inc * 1:
            n -= inc
            ans[pos] = '2'
        pos -= 1
    return ''.join(ans)[::-1]