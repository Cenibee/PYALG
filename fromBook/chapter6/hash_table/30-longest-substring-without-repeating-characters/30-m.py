from typing import Deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        inclueded_char = set()
        result = 0

        for char in s:
            if char not in inclueded_char:
                inclueded_char.add(char)
            else:
                result = max(result, len(inclueded_char))
                while s[head] != char:
                    inclueded_char.remove(s[head])
                    head += 1
                head += 1
        return max(result, len(inclueded_char))


sol = Solution()

print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring("abdacd"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("dvdf"))