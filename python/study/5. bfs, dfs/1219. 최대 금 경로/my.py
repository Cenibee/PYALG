from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        '''
        음.... 일단 리프가 되는 부분에서부터는 리듀스를하고, 그뒤엔 전체 DFS 해서 찾자
        우선 리듀스 뺴고 브루트 포스를 짜보자
          ┌─ m ─┐
        ㅇㅇㅇㅇㅇㅇ
        ㅇㅅㅅㅅㅅㅇ┐
        ㅇㅅㅅㅅㅅㅇn
        ㅇㅅㅅㅅㅅㅇ┘
        ㅇㅇㅇㅇㅇㅇ
        1 ~ m + 1
        '''
        n, m = len(grid), len(grid[0])

        temp = [[0] * (m + 2)]
        grid = temp + [[0] + x + [0] for x in grid] + temp

        r_s = [0, 1, 0, -1]
        c_s = [1, 0, -1, 0]

        def dfs(row:int, col:int) -> int:
            if not grid[row][col]:
                return 0
            val = grid[row][col]
            grid[row][col] = 0
            res = val + max([dfs(row + r_s[x], col + c_s[x]) for x in range(4)])
            grid[row][col] = val
            return res

        ans = 0
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if grid[row][col]:
                    ans = max(ans, dfs(row, col))
        return ans

sol = Solution()
sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])
