from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 길이가 0 이면 빈 문자열 반환
        if not strs: return ''

        # 문자열의 각 자리가 있는지 확인하기
        # 위한 체인 맵을 임의의 단어로 만든다.
        # pop()이 간단하니 pop()으로 마지막 단어 사용
        m = inner = {}
        last = strs.pop()
        for ch in last:
            inner[ch] = {}
            inner = inner[ch]

        # 단어가 1개인 경우 그 단어를 출력하기위해
        # 위에서 체인맵을 만든 단어의 길이를 최초 값으로 설정
        ans = len(last)

        for word in strs:
            inner = m
            common_prefix = 0

            # 단어마다 체인맵에 연쇄 접근하고
            for ch in word:
                # 더 이상 들어갈 수 없을 때
                if ch not in inner: break
                common_prefix += 1
                inner = inner[ch]

            # 깊이가 0인 경우는 끝난거니까 그냥 리턴한다.
            if common_prefix == 0: return ''

            # 접근한 깊이 중 가장 작은 값을 ans로 설정한다.
            ans = min(ans, common_prefix)

        # ans 길이만큼 마지막 문자열을 슬라이싱한다.
        return last[:ans]

sol = Solution()
sol.longestCommonPrefix(["flower","flow","flight"])