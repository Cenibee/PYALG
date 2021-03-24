from typing import List, Set


class Solution:
    # 공간 복잡도 O(nt)|n = len(words), t = [words' avg len]
    def palindromePairs(self, words: List[str]) -> Set[Set[int]]:
        result = set()
        words_dict = {word: i for i, word in enumerate(words)}

        # 펠린드롬 검사를 함수로 구현
        def is_palindrome(word: str) -> bool:
            mid = len(word) // 2
            return word[:mid] == word[:~mid:-1]

        # words 순회
        for word in words:
            # word 앞에 붙였을 때 펠린드롬이 되는 문자 탐색
            sub_word = ''
            for ch in word[::-1] + '\0':
                if sub_word in words_dict\
                        and sub_word != word\
                        and is_palindrome(sub_word + word):
                    result.add((words_dict[sub_word], words_dict[word]))

                sub_word += ch

            # word 뒤에 붙였을 때 펠린드롬이 되는 문자 탐색
            sub_word = ''
            for ch in word + '\0':
                if sub_word in words_dict\
                        and sub_word != word\
                        and is_palindrome(word + sub_word):
                    result.add((words_dict[word], words_dict[sub_word]))

                sub_word = ch + sub_word

        return result

# 다른 사람들 참고해서 만들어본 것 시간 복잡도 O(nk) | n은 words 길이, k는 모든 문자열의 평균 길이