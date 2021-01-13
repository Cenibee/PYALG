def isPalindrome(self, input: str) -> bool:
    def alnum_gen(input:str, index:int, to:int):
        i = index
        while True:
            if i < -1 or i >= len(input):
                return "end"
            if input[i].isalnum():
                yield (i, input[i].lower())
            i = i + to
    head = alnum_gen(input, 0, 1)
    tail = alnum_gen(input, len(input) - 1, -1)
    try:
        while True:
            head_index, head_val = next(head)
            tail_index, tail_val = next(tail)
            if head_index >= tail_index:
                return True
            if head_val != tail_val:
                return False
    except StopIteration: return True

print(isPalindrome(None, "A man, a plan, a canal: Panama"))
print(isPalindrome(None, "A man, a plan, a cnal: Panama"))
print(isPalindrome(None, "*$&%*(#&$%)_@#(*$_@#$"))

# 필터함수 쓸 때 vs 정규식 쓸 때
# 정규식 사용법 간단히 조사
# iterable 과 iterator 종류
# ├─ 필터
# ├─ 컴프리헨션
# └─ 제네레이터
# 문자열 조작 => 슬라이싱!