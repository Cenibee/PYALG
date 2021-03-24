'''
[시작, 종료] 구간이 담긴 배열 intervals 에 대해,
겹치는 구간을 모두 병합하고 커버되는 모든 구간을 구하여라
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        merge = intervals[0]
        for interval in intervals:
            if interval[0] <= merge[1]:
                merge[1] = max(merge[1], interval[1])
            else:
                ans.append(merge)
                merge = interval

        ans.append(merge)
        return ans


sol = Solution()

print(sol.merge([[15,18],[1,3],[8,10],[2,6]]))
print(sol.merge([[1,4],[2,3]]))