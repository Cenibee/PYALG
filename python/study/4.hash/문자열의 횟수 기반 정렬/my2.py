from typing import DefaultDict

class Solution:
    def frequencySort(self, s: str) -> str:
        # 0 초기화 코드를 줄이기 위해 DefaultDict 사용
        m = DefaultDict(int)

        # (문자: 출현 횟수) 형태의 키-값을 생성
        for ch in s: m[ch] += 1

        # (중복 횟수: [문자열 * 중복횟수, ...]) 형태로 키 -값 생성
        count_m = DefaultDict(list)
        for ch, count in m.items():
            count_m[count].append(ch * count)

        # 중복 횟수에 대해 정렬하고 차례대로 append
        ans = []
        for key in sorted(count_m.keys(), reverse=True):
            ans.append(''.join(count_m[key]))

        # join 해서 반환
        return ''.join(ans)

sol = Solution()
sol.frequencySort("tree")
