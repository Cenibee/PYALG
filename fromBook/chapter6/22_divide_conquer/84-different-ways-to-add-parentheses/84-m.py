'''
못 풀었다 나중에 다시 풀어보자
'''

from typing import List, Tuple


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        opers = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        def get_number(s: int, e:int) -> Tuple[int]:
            # 숫자를 탐색한다.
            num_stack = []
            while s < e and input[s] not in opers:
                num_stack.append(input[s])
                s += 1
            return int(''.join(num_stack)), s


        def partial_compute(s: int, e: int) -> List[int]:
            if s == e: return [0]

            ans = []
            num, s = get_number(s, e)

            if s == e: return [num]

            while s < e:
                # 연산자를 고르고
                oper = opers[input[s]]
                s += 1

                # 뒤에 나올 수 잇는 모든 숫자에 대해 연산한 값을 ans 에 저장
                for post_num in partial_compute(s, e):
                    ans.append(oper(num, post_num))

                next_num, s = get_number(s,e)
                num = oper(num, next_num)

            return ans

        return partial_compute(0, len(input))

sol = Solution()
sol.diffWaysToCompute("2*3-4*5")