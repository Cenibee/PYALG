class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        for i in range(len(s) - 1):
            palindrome = self.search_palindrome(s, i, i + 2, palindrome)
            palindrome = self.search_palindrome(s, i, i + 1, palindrome)
        return palindrome

    def search_palindrome(self, s: str, left:int, right:int, palindrome:str) -> str:
        try:
            if s[left] != s[right]:
                return palindrome
            while left > 0 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
        except IndexError: pass

        if right - left > len(palindrome):
            return s[left: right + 1]
        else:
            return palindrome



sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("aaaa"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("ab"))
print(sol.longestPalindrome("ccb"))
print(sol.longestPalindrome("bcc"))
print(sol.longestPalindrome("ccccccccccccccccccccccccccc"))

# 아....