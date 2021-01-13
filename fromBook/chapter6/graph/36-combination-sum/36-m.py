from typing import List

# TODO 중복 숫자
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        알고리즘을 말로 표현해보자
            구현 알고리즘: DFS 를 이용하며, 미리 정렬해서 백트래킹을 이용한다.
            순서
                1. candidates를 오름차순 정렬한다.
                2. DFS 시작
                    - 가장 큰 수(마지막 수)를 첫 노드로 시작한다.
                    - 각 노드에는 목표 숫자인 target이 존재한다.
                    - 각 노드의 하위 노드는 자신과 자신보다 작은 숫자를 가지는 노드다.
                    - 하위 노드의 target은 [상위 노드의 target - 상위 노드의 수]가 된다.
                3-1. target이 0이 되는 노드까지의 경로를 results에 추가하고 하위 경로는 무시한다.
                3-2. target이 0보다 작은 노드는 무시한다.
        '''

        candidates.sort()
        stack = []
        results = []

        def combinations_sum_dfs(pointer: int, target: int):
            # pointer 의 값이 target 보다 크면 pointer--
            while candidates[pointer] > target:
                pointer -= 1
                if pointer < 0:
                    return

            # pointer 의 값이 target 값이면 stack 에 push하고 저장후 바로 pop
            if candidates[pointer] == target:
                results.append(stack[:] + [candidates[pointer]])
                pointer -= 1

            # 재귀 함수 호출 - 중복이 허용되니 pointer를 그대로 해서 호출한다.
            while pointer >= 0:
                stack.append(candidates[pointer])
                combinations_sum_dfs(pointer, target - candidates[pointer])
                stack.pop()
                pointer -= 1

        combinations_sum_dfs(len(candidates) - 1, target)
        return results


sol = Solution()
print(sol.combinationSum([1,2,3,5,7,9], 10))