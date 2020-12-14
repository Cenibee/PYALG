class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        index = 0
        while index  < len(s) - 1:
            test = s[index]
            half_palindrome = ''

            # TODO index + 1이 len -1 보다 크면 진작에 끝내야함
            if s[index] == s[index + 1]:
                test += s[index + 1]
                head, tail = index - 1, index + 2
            else:
                head, tail = index -1, index + 1
            try:
                while head >= 0 and s[head] == s[tail]:
                    half_palindrome += s[head]
                    head -= 1
                    tail += 1
            except IndexError :
                pass

            if (len(half_palindrome) * 2) + len(test) > len(longest):
                longest = half_palindrome + test + half_palindrome[::-1]

            index += 1
        return longest


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("ccccccccccccccccccccccccccc"))
