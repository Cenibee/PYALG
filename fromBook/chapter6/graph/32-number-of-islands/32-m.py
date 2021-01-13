from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        n * m 탐색 하면서 0이면 패스 1이면 연결된 1들을 전부 0으로 바꿔주고 count += 1
        탐색 방향 순서는 오 아 왼 위로 하고 0으로 바꾸고 다음 스택으로 넘어간다.
        '''

        height = len(grid)
        width = len(grid[0])
        count = 0

        def remove_island(m: int, n: int):
            if m < 0 or n < 0 or \
                m >= height or n >= width or \
                grid[m][n] == '0':
                    return
            grid[m][n] = "0"
            remove_island(m + 1, n)
            remove_island(m, n + 1)
            remove_island(m - 1, n)
            remove_island(m, n - 1)

        for m in range(height):
            for n in range(width):
                if grid[m][n] == '1':
                    count += 1
                    remove_island(m, n)

        return count

sol = Solution()
grid = [
    ["1","0","1","1","0","1","1"]
]
print(sol.numIslands(grid=grid))
for l in grid:
    print(l)