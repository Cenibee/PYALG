from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # k = 1 일 땐 1~n 까지 모든 수 하나만 가지는 리스트의 리스트
        if k == 1:
            return [[x] for x in range(1, n + 1)]

        # n 이 포함된 모든 조합
        result = self.combine(n - 1, k - 1)
        for prev_comb in result:
            prev_comb.append(n)

        # n 이 포함되지 않은 모든 조합
        if n - 1 >= k:
            others = self.combine(n - 1, k)
            for others_comb in others:
                result.append(others_comb)

        return result





sol = Solution()
print(sol.combine(4, 2))
a = []