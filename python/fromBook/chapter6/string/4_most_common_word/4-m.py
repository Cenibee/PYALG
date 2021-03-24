# https://leetcode.com/problems/most-common-word/

from typing import Counter, List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        filtered_paragraph = re.sub(r'\s*([!\?\',;\.]+)\s*', ' ', paragraph).lower()
        tokens = filtered_paragraph.split()
        # for (most_common, count) in Counter(tokens).most_common():
        #     if(banned.count(most_common) == 0):
        #         return most_common
        sorted_words = sorted(Counter(tokens).items(), key=lambda x: x[1], reverse=True)
        banned_set = set(banned)
        for word, ignore in sorted_words:
            if word not in banned_set:
                return word

sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))

# 어떤 리스트를 만든다 -> 리스트 컴프리헨션
# 오... 내가 더 빠름.... 메모리도... 낮음.. 오....
# 참고했을 때 생각해 볼 사항
# ├─ banned를 set(banned) 로 변환해서 사용해서 시간을 낮췄다. 물론 멤은 올라갔겠지만
# └─ Counter의 most_common 함수는 생각보다 시간이 좀 걸리는 것 같다.
#    ├─ 뭔가의 카운팅을 O(1) 시간 복잡도로 여러번 가져오는 경우 좋겠지만, 그 외의 경우에는 직접 찾는게 빠를듯?
#    └─ 헤비한 문제에서는 가독성을 위해 사용하는게 좋겠지만 라이트한 문제에서는 직접 찾는게 빠르겠다.
