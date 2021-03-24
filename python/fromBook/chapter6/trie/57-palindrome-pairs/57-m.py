from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        for i, word in enumerate(words):
            for o, word2 in enumerate(words):
                if i == o:
                    continue
                new_word = word + word2
                mid = len(new_word) // 2
                if new_word[:mid] == new_word[-1:-mid - 1:-1]:
                    result.append([i, o])

        return result


sol = Solution()
sol.palindromePairs(["abcd","dcba","lls","s","sssll","sl"])

# 시간 초과 n^2