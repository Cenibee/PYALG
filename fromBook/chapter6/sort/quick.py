from typing import List

def partition(arr: List[int]):
    pivot = arr[len(arr) - 1]
    i = 0
    for j in range(len(arr)):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[len(arr) - 1] = arr[len(arr) - 1], arr[i]
    return i

def quick_sort(arr: List[int]):
    if len(arr) > 1:
        pivot = partition(arr)
        return quick_sort(arr[:pivot]) + quick_sort(arr[pivot:])
    else:
        return arr


a = [6,4,2,1,7,8,3,9,0,5]
print(quick_sort(a))