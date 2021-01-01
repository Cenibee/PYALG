from typing import List, Tuple

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        result = [0] * length
        head = 0
        def sub_function(head: int, result:List[int]) -> int:
            p = head + 1
            if p >= length:
                return p
            if T[head] < T[p]:
                result[head] = 1
                return p

            while p < length and T[head] >= T[p]:
                p = sub_function(p, result)

            if p < length:
                result[head] = p - head
            return p

        while head < length:
            head = sub_function(head, result)

        return result

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))




