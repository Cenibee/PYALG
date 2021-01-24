'''
정수 n 과 start가 주어졌을 때
nums 배열 크기 n , 각 원소는 start + 2*i
'''

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for num in (start + 2*x for x in range(n)):
            ans ^= num
        return ans