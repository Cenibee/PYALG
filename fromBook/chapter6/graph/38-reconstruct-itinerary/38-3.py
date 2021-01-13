from typing import DefaultDict, List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = DefaultDict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]

sol = Solution()

print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"],["JFK","TES"],["TES","JFK"]]))
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"],["JFK","TES"],["TES","JFK"]]))
print(sol.findItinerary([["JFK","NRT"],["NRT","JFK"],["JFK","NRT"],["NRT","JFK"],["JFK","TES"],["TES","JFK"]]))
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))