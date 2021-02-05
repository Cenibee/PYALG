from typing import DefaultDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = DefaultDict(int)
        max_frequency = 0

        for i, char in enumerate(s):
            counts[char] += 1
            if counts[char] > max_frequency:
                max_frequency = counts[char]
            else:
                cur_len = max_frequency + k
                if i >= cur_len:
                    start = s[i - cur_len]
                    counts[start] -= 1

        return min(len(s), max_frequency)

sol = Solution()
print(sol.characterReplacement("AABBAABB",1))