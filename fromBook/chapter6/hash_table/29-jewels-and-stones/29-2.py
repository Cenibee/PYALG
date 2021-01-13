from typing import DefaultDict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = DefaultDict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count