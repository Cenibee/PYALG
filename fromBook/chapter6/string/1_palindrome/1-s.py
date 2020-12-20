class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = "".join(filter(str.isalnum, s)).lower()
        return filtered_str == filtered_str[::-1]

print(Solution.isPalindrome(None, "A man, a plan, a canal: Panama"))
print(Solution.isPalindrome(None, "A man, a plan, a cnal: Panama"))
print(Solution.isPalindrome(None, "*$&%*(#&$%)_@#(*$_@#$"))