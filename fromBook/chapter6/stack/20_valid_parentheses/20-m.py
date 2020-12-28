class Solution:
    def isValid(self, s: str) -> bool:
        head, tail = '([{', ')]}'
        stack = []

        for ch in s:
            if ch in head:
                stack.append(ch)

            # 인풋의 조건이 ([{}])이므로 별도의 조건은 생략
            elif len(stack) == 0 or head.index(stack.pop()) != tail.index(ch):
                return False

        return len(stack) == 0


sol = Solution()

print(sol.isValid('()[]{}'))
print(sol.isValid(')[]{}'))
print(sol.isValid('([]{})'))
print(sol.isValid('()[]{})'))

print(sol.isValid('(()()(()()))'))
