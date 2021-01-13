import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations([x for x in range(1, n + 1)], k))