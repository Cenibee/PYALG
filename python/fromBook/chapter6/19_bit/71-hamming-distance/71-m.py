class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return len(list(filter(lambda x: x == '1', bin(x ^ y))))