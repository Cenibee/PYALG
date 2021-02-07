from typing import DefaultDict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        m = DefaultDict(list)
        for person in people:
            m[person[1]].append(person)
        ans = sorted(m.pop(0), key=lambda x: x[0])
        for k in sorted(m.keys()):
            for h, _ in sorted(m[k], reverse=True):
                count = 0
                for i, (comp, _) in enumerate(ans):
                    if comp >= h:
                        count += 1
                    if count == k:
                        ans.insert(i + 1, (h, k))
        return ans

'''
사용한 알고리즘 순서
1. 딕셔너리 m을 만들어 k 값을 키로 가지는 리스트를 만든다.
2. m[0] 를 정렬해 ans로 초기화 한다.
3. m[1:] 를 순서대로 순회하면서 큰 값 부터 알맞은 위치에 넣는다.

con
<<<<<<< HEAD
아무래도 정렬이 너무 많은데... 어떻게 최적화 할 수 있을까?
=======
너무 회문 중첩이 많고, 정렬이 과도하게 많은 느낌이다.
k 말고 h를 기준으로 딕셔너리를 만들어도 된다면, 시간이 더 최적화 될 것 같다.
>>>>>>> 6080d8ed57cf47ee0c95d63dbd4c16951ddc3cbb
'''