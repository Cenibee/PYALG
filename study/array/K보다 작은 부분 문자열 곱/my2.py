'''
leetcode 713 - Subarraay Product less Than K (K 보다 작은 부분 문자열 곱)
https://leetcode.com/problems/subarray-product-less-than-k/

양수로만 이루어진 배열 nums가 있다.
모든 원소의 곱이 k보다 작은 부분 문자열의 개수를 구하여라
'''
from typing import DefaultDict, List

class Solution:
    count = 0
    prev_f = -1
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        - k 보다 작은 모든 부분 문자열 집합을 S라 하고, 이에 속하는 어떤 원소를 s_i 라 부른다.
        - s_i의 부분 문자열 개수를 N(s_i) 함수로 정의한다.
        1. 어떤 s_i의 모든 부분 문자열은 S에 속한다.
        2. 따라서 s_m 과 s_n에 겹치는 문자가 x 개라면, s_m과 s_n이 커버하는 부분의 부분 문자열 개수는 N(s_m) + N(s_m) - N([겹치는 부분])
        '''

        def total_substr(n: int):
            return (n * (n + 1)) // 2

        def countup(t: int, f: int):
            self.count += total_substr(f - t + 1)
            if self.prev_f >= t:
                self.count -= total_substr(self.prev_f - t + 1)
            self.prev_f = f


        start = last = 0
        product = nums[last]


        while last < len(nums) - 1 or product >= k:
            if product < k:
                last += 1
                product *= nums[last]
            elif last == start:
                start, last = start + 1, last + 1
                if last >= len(nums):
                    break
                product = nums[last]
            else:
                countup(start, last - 1)
                while product >= k and start < len(nums):
                    product //= nums[start]
                    start += 1
        while product >= k and start < len(nums):
            product //= nums[start]
            start += 1
        if product < k:
            countup(start, last)

        return self.count





sol = Solution()
print(sol.numSubarrayProductLessThanK(nums = [1,2,3], k = 0))
print(sol.numSubarrayProductLessThanK([1,2,10,11,12,1,2,3], 5))
print(sol.numSubarrayProductLessThanK(nums = [10, 5, 2, 6], k = 100))
print(sol.numSubarrayProductLessThanK([4,5,2,6,3,8,9,7,10], 200))