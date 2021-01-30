'''
leetcode 844. 백스페이스 문자열 비교
https://leetcode.com/problems/backspace-string-compare/
두 문자열 S 와 T 에 대해, 두 문자열을 에디터에 타이핑하면 같은 문자인지를 반환하라.
단, '#' 이 백스페이스를 뜻하고, 빈 문자열에 백스페이스를 하면 그대로 빈 문자열이다.
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 문자열을 읽고 백스페이스를 수행해 리스트로 만드는 함수
        def proc_bs(input: str) -> list:
            stack = []
            for ch in input:
                # 백스페이스가 아니면 stack 에 push
                if ch != '#':
                    stack.append(ch)
                # 백스페이스고, stack 이 비어있지 않으면 pop 해서 문자를 제거
                elif stack:
                    stack.pop()
            return stack

        # 각 문자에대해 백스페이스를 실행한 결과가 같은지 비교한다.
        return proc_bs(S) == proc_bs(T)

sol = Solution()
sol.backspaceCompare("y#fo##f", "y#f#o##f")