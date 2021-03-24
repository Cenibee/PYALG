class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        소문자로만 이루어진 문자열 s 에 대해, 중복되는 문자는 하나만 남기고 제거한 모든 문자열 집합 중,
        사전상 가장 먼저 나오는 문자열을 구하라
        '''
        a = {}

        