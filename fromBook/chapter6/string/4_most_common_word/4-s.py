from typing import Counter, List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall('\w+', paragraph.lower())
        for word, count in sorted(Counter(words).items(), key=lambda x: x[1], reverse=True):
            if word not in banned:
                return word

sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))