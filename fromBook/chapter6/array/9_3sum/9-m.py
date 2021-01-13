from typing import List
import math

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums 의 어떤 세 요소 a, b, c 에 대해 `a + b + c = 0` 을 만족하는 abc 쌍을 구하라
        겹치는 조합의 쌍은 허용하지 않는다.
        '''
        # 3개 미만이면 쌍이 존재할 수 없다
        if len(nums) < 3:
            return []
        result = []

        # 정렬하고 초기 포인터를 세팅한다.
        nums.sort()
        head, tail = 0, len(nums) - 1
        finder = head + 1

        # head, tail 포인터를 쪼이면서 요구사항을 만족하는 쌍을 찾는 반복문
        while head < finder and finder < tail:
            two_sum = nums[head] + nums[tail]
            step, to = (1, tail + 1) if two_sum < 0 else (-1, head - 1)

            # two_sum + nums[finder] 값의 최소 절대값을 갖는 finder를 찾는다
            # two_sum 이 음수면 양의 방향, 양수면 음의 방향으로 진행한다
            for i in range(finder + step, to, step):
                if(i == tail or i == head):
                    finder = i - step
                    break
                elif abs(two_sum + nums[i]) < abs(two_sum + nums[i + step]):
                    finder = i
                    break

            # 절대값이 0 이었으면 결과 리스트에 추가한다
            if two_sum + nums[finder] == 0 and result.count([nums[head], nums[finder], nums[tail]]) == 0:
                result.append([nums[head], nums[finder], nums[tail]])
            # 모든 포인터가 0을 가르키면 더 이상 진행할 필요가 없다
            if nums[head] == nums[finder] and nums[finder] == nums[tail]:
                break

            # head, tail, finder를 업데이트한다
            if two_sum + nums[finder] < 0:
                head += 1
            elif two_sum + nums[finder] > 0:
                tail -= 1
            elif two_sum + nums[finder] == 0:
                tail -= 1
                head += 1

            if head == finder:
                finder += 1
            elif tail == finder:
                finder -= 1

        return result

sol = Solution()
print(sol.threeSum([]))
print(sol.threeSum([0]))
print(sol.threeSum([1, 2]))
print(sol.threeSum([-1,0,1]))
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,0,0,0,0,0]))
print(sol.threeSum([-2,0,1,1,2]))
print(sol.threeSum([-2,-1,-1,0,1,2]))
print(sol.threeSum([-2,0,0,2,2]))
print(sol.threeSum([3,0,-2,-1,1,2]))

# 투포인터를 이용했는데 이거로는 못풀것 같은디