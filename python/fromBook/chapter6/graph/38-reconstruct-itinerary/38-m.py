from typing import DefaultDict, List
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = DefaultDict(list)

        for ticket in tickets:
            depature = ticket[0]
            arrival = ticket[1]
            arrival_list = ticket_dict[depature]
            i = len(arrival_list)
            for (index, arrival_elem) in enumerate(arrival_list):
                if arrival_elem[0] > arrival:
                    i = index
                    break
            ticket_dict[depature].insert(i, [arrival, True])

        result = []

        def dfs(departure: str):
            result.append(departure)

            for arrival in ticket_dict[departure]:
                if arrival[1]:
                    arrival[1] = False
                    dfs(arrival[0])
                    arrival[1] = True

            if len(result) != len(tickets) + 1:
                result.pop()

        dfs('JFK')
        return result

sol = Solution()

print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"],["JFK","TES"],["TES","JFK"]]))
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"],["JFK","TES"],["TES","JFK"]]))
print(sol.findItinerary([["JFK","NRT"],["NRT","JFK"],["JFK","NRT"],["NRT","JFK"],["JFK","TES"],["TES","JFK"]]))
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(sol.findItinerary([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]))
