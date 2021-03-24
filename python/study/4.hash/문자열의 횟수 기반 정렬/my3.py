from typing import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Counter로 aggregate 하고
        counter = Counter(s).most_common()
        ans = []
        # count 만큼 곱해서 append로 모은 후
        for ch, cnt in counter:
            ans.append(ch * cnt)
        # join 하여 반환
        return ''.join(ans)