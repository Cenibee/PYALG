from typing import List
def bubble_sort(arr: List[int]):
    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j-1]

a = [6,4,2,1,7,8,3,9,0,5]
bubble_sort(a)
print(a)