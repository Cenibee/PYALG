# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

input = ["H","a","n","n","a","h"]
sol = Solution()
sol.reverseString(input)
print(input)
