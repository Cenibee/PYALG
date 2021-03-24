'''
leetcode 713 - Subarraay Product less Than K (K 보다 작은 부분 문자열 곱)
https://leetcode.com/problems/subarray-product-less-than-k/

양수로만 이루어진 배열 nums가 있다.
모든 원소의 곱이 k보다 작은 부분 문자열의 개수를 구하여라
'''
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        시간 복잡도는 O(n^2) - a 가 나오지 않을까
        '''
        count = 0
        for start in range(len(nums)):
            product = 1
            for pointer in range(start, len(nums)):
                product *= nums[pointer]
                if product < k:
                    count += 1
                else:
                    break

        return count

# try1: 시간복잡도 최적화가 안됨