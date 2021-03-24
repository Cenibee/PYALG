from typing import DefaultDict, List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        [0 ~ n-1] 도시 중 src -> dst 도시를 가는 flights를 통한 경로 중 k 번 이하 거쳐서 갈 수 있는 가장 싼경로
        BFS로 탐색하다가 dst 발견 했을 때 K 보다 작으면 무시 아니면 리턴
        '''
        graph = DefaultDict(list)

        for source, dest, price in flights:
            graph[source].append([price, dest])

        priority_q = [[0, -1, src]]

        while priority_q:
            price, stops, city = heapq.heappop(priority_q)

            if city == dst and stops <= K:
                return price
            elif stops >= K:
                continue

            for next_price, next_city in graph[city]:
                total_price = price + next_price
                heapq.heappush(priority_q, [total_price, stops + 1, next_city])

        return -1


sol = Solution()

print(sol.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
