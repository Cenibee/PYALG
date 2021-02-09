from typing import List, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        for needs in Counter(tasks).values():
            heapq.heappush(heap, -needs)
        process = 0
        while heap:
            temp = []
            for _ in range(n + 1):
                if not heap and not temp: break
                process += 1

                if not heap: continue
                needs = heapq.heappop(heap)
                if needs < -1:
                    temp.append(needs + 1)
            for task in temp:
                heapq.heappush(heap, task)
        return process




sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"],2))