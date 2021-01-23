'''
문자열이 주어졌을 때, 펠린드롬 부분 문자열이 몇 개가 있는지 세어라
같은 부분 문자열이라도 시작, 종료 인덱스가 다르다면 다른 문자열로 센다.

팰린드롬의 최적화 같은 숫자들은 묶어서 comb로 수를 구할 수 있다.
'''
from itertools import permutations


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0
        count = 0
        while i < n:
            l = r = i
            while r < n and s[r] == s[i]: r += 1
            while l >= 0 and s[l] == s[i]: l -= 1
            i = r

            m = r - l
            count += (m * (m - 1)) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count

sol = Solution()
print(sol.countSubstrings('aaaaa'))
print(sol.countSubstrings('abcasdawd'))