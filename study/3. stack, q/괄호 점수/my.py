'''
leetcode 856. 괄호 점수
https://leetcode.com/problems/score-of-parentheses/
유효한 괄호로 이루어진 문자열 S 에 대해,
아래 규칙에 따라 점수를 계산하여라
    - () 는 1점을 갖는다.
    - 유효한 괄호 문자열 A 와 B 에 대해, AB 는 A + B 점을 갖는다.
    - 유효한 괄호 문자열 A 에 대해, (A) 는 2*A 점을 갖는다.
'''

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # 스택을 하나 생성한다.
        stack = []

        # 모든 괄호에 대해 순회한다.
        for p in S:
            # '('면 스택에 push 한다. - 문자/숫자를 섞지 않도록 0으로 사용한다.
            if p == '(':
                stack.append(0)
                continue

            # ')'면 아래 stack에서 pop한다.
            el = stack.pop()

            # '(' 이 아니라면 '(' 까지 값들을 모두 더해 val를 만들고 -- 규칙 2번
            # val * 2 를 스택에 push 한다. -- 규칙 3번
            if el:
                val = 0
                while el:
                    val += el
                    el = stack.pop()
                stack.append(val * 2)
            # '(' 이라면 1을 스택에 push 한다. -- 규칙 3번
            else:
                stack.append(1)

        # 모든 괄호를 읽은 후 스택에 남아있는 점수들을 합산하여 반환한다.
        ans = 0
        for score in stack: ans += score
        return ans


sol = Solution()
sol.scoreOfParentheses('()')
sol.scoreOfParentheses('(()(()))')