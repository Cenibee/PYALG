class Solution:
    def climbStairs(self, n: int) -> int:
        way, way_before = 1, 1

        for _ in range(n - 1):
            way, way_before = way + way_before, way

        return way