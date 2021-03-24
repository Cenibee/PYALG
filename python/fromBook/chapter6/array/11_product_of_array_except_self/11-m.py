from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        길이가 n > 1을 만족하는 배열 nums에 대해, output[i] 가 nums에서 num[i]를 제외한 모든 수의 곱인 output을 구하시오
        나누기를 사용하지 않고 O(n) 시간복잡도를 가지도록 구현하세요
        '''
        left, right = 1, 1

        size = len(nums)
        output = [1] * size

        for i in range(size - 1):
            left *= nums[i]
            right *= nums[~i]

            output[i + 1] *= left
            output[~i - 1] *= right
        return output

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))