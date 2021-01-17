from typing import DefaultDict, Deque, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        n 개의 정점(0 ~ n-1)과 n-1개의 간선(e[0] = (a0, b0))이 주어졌을 때, 최소 높이를 갖는 트리를 만드는 루트 노드 X를 구하시오.
        '''
        if n == 1:
            return [0]
        graph = {}
        for a, b in edges:
            if a in graph: graph[a].append(b)
            else: graph[a] = [b]
            if b in graph: graph[b].append(a)
            else: graph[b] = [a]

        last_nodes = Deque()

        while graph:
            last_nodes.clear()

            for key in list(graph):
                if len(graph[key]) == 1:
                    last_nodes.append((key, graph.pop(key)[0]))
                elif len(graph[key]) == 0:
                    return [key]
            for _ in range(len(last_nodes)):
                key, val = last_nodes.popleft()
                last_nodes.append(key)
                graph[val].remove(key)
        return last_nodes

sol = Solution()

print(sol.findMinHeightTrees(n = 6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]))