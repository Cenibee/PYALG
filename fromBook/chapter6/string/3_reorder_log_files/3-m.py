# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import Deque, List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        1. 모든 문자 로그가 숫자 로그 앞에 오도록 한다.
        2. 문자 로그 순서는 상관없이, 숫자는 오름차순
        '''
        # 1. 디큐로 구현 후 변환
        # ret = Deque()
        # for log in logs:
        #     if(log[log.index(' ') + 1].isalpha()):
        #         ret.appendleft(log)
        #     else:
        #         ret.append(log)
        # return list(ret)

        # 2. list 두개 만들어서 concat
        letter_logs = []
        digit_logs = []
        for log in logs:
            if(log[log.index(' ') + 1].isalpha()):
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        return letter_logs + digit_logs

sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))