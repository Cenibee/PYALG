'''
알파벳 대문자로만 이루어진 문자열 s 에 대해, 최대 k 번의 연산을 수행할 수 있다.
한 번의 연산에서는, 문자열의 아무 문자를 선택하고, 아무 대문자 알파벳 문자로 교환할 수 있다.

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        checker = {}
        ans = 0
        for i, ch in enumerate(s):
            # ch 가 첫 등장했다면, 현 좌표를 찍고, 점핑을 0으로 해서 put
            if ch not in checker:
                checker[ch] = [i, i, 0]
                continue

            left, right, jumping = checker[ch]
            next_jump = jumping + (i - right - 1)

            # 점핑 합계가 k 보다 작거나 같으면 업데이트만
            if next_jump <= k:
                checker[ch] = [left, i, next_jump]
                continue

            # 점핑 합계가 K 보다 크면 남은 점핑은 빼고 + k
            ans = max(ans, right - left + 1 - jumping + k)

            while left < right:
                left += 1
                if s[left] == ch and next_jump <= k:
                    break
                elif s[left] != ch:
                    next_jump -= 1
            checker[ch] = [left, i, next_jump]
        ans = max(ans, max(y - x + k - z + 1 for x, y, z in checker.values()))
        return ans if ans <= len(s) else len(s)

sol = Solution()
print(sol.characterReplacement('ABAB', 2))
print(sol.characterReplacement('AABABBA', 1))
print(sol.characterReplacement("ALKSJDKASKJSSASASWKDWJJJASDJASDJ",5))
