# 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

print(isPalindrome(None, "A man, a plan, a canal: Panama"))
print(isPalindrome(None, "A man, a plan, a cnal: Panama"))
print(isPalindrome(None, "*$&%*(#&$%)_@#(*$_@#$"))