from typing import DefaultDict, Deque, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        n 개의 정점(0 ~ n-1)과 n-1개의 간선(e[0] = (a0, b0))이 주어졌을 때, 최소 높이를 갖는 트리를 만드는 루트 노드 X를 구하시오.
        '''
        if n == 1:
            return [0]
        graph = DefaultDict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        last_nodes = None

        while graph:
            last_nodes = Deque()

            for key in list(graph):
                if len(graph[key]) == 1:
                    last_nodes.append((key, graph.pop(key).pop()))

            if len(graph) == 1:
                return [x for x in graph]
            if len(graph) == 0:
                return [x[0] for x in last_nodes]

            for _ in range(len(last_nodes)):
                key, val = last_nodes.popleft()
                last_nodes.append(key)
                graph[val].remove(key)
        return last_nodes

sol = Solution()

print(sol.findMinHeightTrees(n = 6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]))
print(sol.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
print(sol.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(sol.findMinHeightTrees(n = 1, edges = []))
print(sol.findMinHeightTrees(n = 2, edges = [[0,1]]))