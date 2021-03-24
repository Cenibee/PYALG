from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

input = ["H","a","n","n","a","h"]
sol = Solution()
sol.reverseString(input)
print(input)

# 슬라이싱은 리스트에서도 사용할 수 있다!!