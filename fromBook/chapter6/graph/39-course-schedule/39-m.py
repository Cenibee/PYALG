from typing import DefaultDict, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = DefaultDict(list)

        for precourse, course in prerequisites:
            graph[precourse].append(course)

        def dfs_cycle(precourse: int, root_course: int) -> bool:
            if precourse == root_course:
                return True
            while graph[precourse]:
                if dfs_cycle(graph[precourse].pop(), root_course):
                    return True
            return False


        for precourse in range(numCourses):
            if graph[precourse] and\
                dfs_cycle(graph[precourse].pop(), precourse):
                    return False

        return True

sol = Solution()
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(2, [[1,0],[0,1]]))
print(sol.canFinish(3, [[1,0],[1,2],[0,1]]))
print(sol.canFinish(4, [[0,1],[3,1],[1,3],[3,2]]))