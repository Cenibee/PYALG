import re


def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

print(isPalindrome(None, "A man, a plan, a canal: Panama"))
print(isPalindrome(None, "A man, a plan, a cnal: Panama"))
print(isPalindrome(None, "*$&%*(#&$%)_@#(*$_@#$"))