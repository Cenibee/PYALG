import bisect
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        stack = [(0, 0, True)]

        while stack:
            row, col, search_row = stack.pop()

            if search_row:
                nxt = bisect.bisect_left(matrix[row], target, col)
                if nxt < col_len and matrix[row][nxt] == target:
                    return True
                for i in range(col, nxt):
                    stack.append((row, i, False))
            else:
                nxt = bisect.bisect_left([matrix[x][col] for x in range(col_len)], target, row)
                if nxt < row_len and matrix[nxt][col] == target:
                    return True
                for i in range(row, nxt):
                    stack.append((i, col, True))

        return False


sol = Solution()
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))

# 이렇게는 하다보니까 중복이 발생할 수 있어 비효율적일거같다 한쪽은 n, 다른 한쪽만 log n을 쓰게해서 중복 없는게 빠를듯