from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        alpha_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        size = len(digits)
        temp = [''] * size
        def add_combines(cur_index: int):
            for i in alpha_dict[digits[cur_index]]:
                temp[cur_index] = i
                if cur_index + 1 == size:
                    result.append(''.join(temp))
                else:
                    add_combines(cur_index + 1)
        add_combines(0)
        return result
