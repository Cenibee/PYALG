from typing import DefaultDict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map = DefaultDict(int)
        for stone in stones:
            hash_map[stone] += 1
        result = 0
        for jewel in jewels:
            result += hash_map[jewel]

        return result