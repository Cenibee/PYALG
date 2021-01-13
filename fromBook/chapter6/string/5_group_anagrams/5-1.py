from collections import defaultdict
from typing import DefaultDict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = DefaultDict(list)
        for word in strs:
            anagram_dict["".join(sorted(word))].append(word)
        return anagram_dict.values()

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))
