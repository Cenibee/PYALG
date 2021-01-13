# 데크 자료형을 이용한 최적화
import collections
from typing import Deque


def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

print(isPalindrome(None, "A man, a plan, a canal: Panama"))
print(isPalindrome(None, "A man, a plan, a cnal: Panama"))
print(isPalindrome(None, "*$&%*(#&$%)_@#(*$_@#$"))