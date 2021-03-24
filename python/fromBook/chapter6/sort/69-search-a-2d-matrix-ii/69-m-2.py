from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row [0] > target: break

            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True

        return False


sol = Solution()
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
print(sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))