class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif len(stack) == 0:
                return False
            elif ch == ')' and '(' != stack.pop():
                return False
            elif ch == '}' and '{' != stack.pop():
                return False
            elif ch == ']' and '[' != stack.pop():
                return False
        return len(stack) == 0

sol = Solution()

print(sol.isValid('()[]{}'))
print(sol.isValid(')[]{}'))
print(sol.isValid('([]{})'))
print(sol.isValid('()[]{})'))

print(sol.isValid('(()()(()()))'))