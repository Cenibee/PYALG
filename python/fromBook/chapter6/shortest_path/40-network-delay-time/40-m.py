from typing import DefaultDict, Deque, List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = DefaultDict(list)
        for source, target, time in times:
            edges[source].append([target, time])

        node_time = {k: 0}
        search_q = Deque()
        search_q.append((k, 0))

        while search_q:
            node, path_time = search_q.popleft()
            for target, edge_time in edges[node]:
                new_time = path_time + edge_time

                if target in node_time:
                    new_time = min(new_time, node_time[target])

                if target not in node_time or new_time < node_time[target]:
                    search_q.append([target, new_time])

                node_time[target] = new_time

        if len(node_time) != n:
            return -1
        else:
            return max(node_time.values())

sol = Solution()
print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(sol.networkDelayTime([[1,2,1]], n = 2, k = 1))
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
