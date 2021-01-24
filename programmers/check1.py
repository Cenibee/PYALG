def solution(strings:list[str], n:int):
    strings.sort(key=lambda x: x[n] + x)
    return strings