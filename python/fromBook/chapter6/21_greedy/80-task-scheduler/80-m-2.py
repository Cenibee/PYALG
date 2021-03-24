from typing import List, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        most_common = counter.most_common(1)
        max_count = list(counter.values()).count(most_common[0][1])
        return max(len(tasks), (n + 1) * (most_common[0][1] - 1) + max_count)
sol = Solution()
sol.leastInterval(["B","C","D","E","F","G","A","A","A","A","A","A"],2)
sol.leastInterval(["A","A","A","B","B","B"],0)


