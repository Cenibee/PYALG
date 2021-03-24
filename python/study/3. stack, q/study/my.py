'''
leetcode 496. 인접한 중복 문자열 제거
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
소문자로만 이루어진 문자열 S 에 대해 두 개의 문자가 인접해 있는 경우 그 문자들을 제거하라.
제거할 수 있는 문자가 없을 때까지 S 에 대해 반복해서 시행한다.
모든 중복이 제거된 문자를 반환한다. 정답은 반드시 한가지라고 보장된다.
'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)