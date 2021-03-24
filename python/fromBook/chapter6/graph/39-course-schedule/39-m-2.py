from typing import DefaultDict, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = DefaultDict(list)

        for precourse, course in prerequisites:
            graph[precourse].append(course)

        visited = set()

        def has_cycle(pre_course: int):
            if pre_course in visited:
                return True

            visited.add(pre_course)
            while pre_course in graph and graph[pre_course]:
                if has_cycle(graph[pre_course].pop()):
                    return True
            visited.remove(pre_course)
            return False

        for course in graph:
            if has_cycle(course):
                return False
        return True