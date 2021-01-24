'''
leetcode 287 - Find the Duplicat Number (중복 숫자 찾기)
https://leetcode.com/problems/find-the-duplicate-number/

정수 배열 nums는 [1, n] 사이의 정수가 모두 포함된 n + 1 길이의 배열이다.
nums 에는 단 하나의 중복되는 숫자가 포함되어있다.
이 중복되는 숫자를 반환하라

'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checker = set()
        for i in nums:
            if i in checker:
                return i
            else:
                checker.add(i)