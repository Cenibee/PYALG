from typing import Counter, List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[\W]', ' ', paragraph)
            .lower().split()
            if word not in banned]
        return Counter(words).most_common(1)[0][0]

sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))