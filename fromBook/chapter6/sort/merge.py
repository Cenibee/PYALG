from typing import Deque, List

def merging_sort(arr: List[int]):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    left = Deque(merging_sort(arr[:mid]))
    right = Deque(merging_sort(arr[mid:]))
    ret = []
    while left and right:
        if left[0] >= right[0]:
            ret.append(right.popleft())
        else:
            ret.append(left.popleft())
    if left: ret += left
    if right: ret += right
    return ret


a = [6,4,2,1,7,8,3,9,0,5]
print(merging_sort(a))