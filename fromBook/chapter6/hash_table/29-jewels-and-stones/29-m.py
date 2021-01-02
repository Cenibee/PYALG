from typing import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(list(stones))

        result = 0
        for jewel in jewels:
            result += counter[jewel]

        return result


sol = Solution()
sol.numJewelsInStones("aA", stones = "aAAbbbb")