'''
leetcode 647 - Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
문자열이 주어졌을 때, 펠린드롬 부분 문자열이 몇 개가 있는지 세어라
같은 부분 문자열이라도 시작, 종료 인덱스가 다르다면 다른 문자열로 센다.
'''
import itertools

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_plndr(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s)\
                and s[left] == s[right]:
                    count, left, right = count + 1, left - 1, right + 1
            return count

        point = count = 0
        for _ in range(len(s)):
            count += 1 + count_plndr(point, point + 1)\
                    + count_plndr(point - 1, point + 1)
            point += 1

        return count

sol = Solution()
print(sol.countSubstrings('aaaaa'))
print(sol.countSubstrings('abcasdawd'))