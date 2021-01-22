class Solution:
    def palindromePairs(self, words: List[str]) -> Set[Set[int]]:
        words_dict = {}
        trie = {}

        result = set()

        palindromes = []
        def palindrome_exists(trie: map, word_stack: List[str] = None):
            if not word_stack:
                word_stack = []
            elif '\0' in trie and self._is_palindrome(word_stack):
                palindromes.append(''.join(word_stack))

            for ch, in trie:
                word_stack.append(ch)
                palindrome_exists(trie[ch], word_stack)
                word_stack.pop()

        # 전처리 - words 순회: O(words * [avg_len])
        for i, word in enumerate(words):
            # words의 인덱스에 빠르게 접근하기 위해 dict 이용
            words_dict[word] = i

            # words를 이용한 trie 자료구조 구성
            node = trie
            for ch in word + '\0':
                if ch not in node:
                    node[ch] = {}
                node = node[ch]

        for idx, word in enumerate(words):
            node = trie
            full_searched = True
            for i, ch in enumerate(word[::-1] + '\0'):
                if '\0' in node:
                    if word[:~i:-1] != word and self._is_palindrome(word[~i::-1]):
                        result.add((words_dict[word[:~i:-1]], idx))
                if ch != '\0':
                    if ch not in node:
                        full_searched = False
                        break
                    node = node[ch]
            if full_searched:
                palindrome_exists(node)

                for palindrome in palindromes:
                    result.add((words_dict[word[::-1] + palindrome], idx))
                palindromes = []

        return result

    def _is_palindrome(self, word: str) -> bool:
        mid = len(word) // 2
        return word[:mid] == word[:~mid:-1]

# Trie에 너무 집착한 것인가.... 너무 복잡하다 simple is the bestㅠㅠㅠ