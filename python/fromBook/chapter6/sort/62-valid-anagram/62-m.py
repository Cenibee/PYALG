from typing import DefaultDict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}

        for ch in s:
            if ch in m:
                m[ch] += 1
            else:
                m[ch] = 1

        for ch in t:
            if ch in m:
                m[ch] -= 1
                if not m[ch] : m.pop(ch)
            else:
                return False
        return len(m) == 0
