from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mid_byte = 0
        for byte in data:
            if mid_byte:
                mid_byte -= 1
                if not (128 <= byte < 192):
                    return False
            elif 240 <= byte < 248:
                mid_byte = 3
            elif 224 <= byte < 240:
                mid_byte = 2
            elif 192 <= byte < 224:
                mid_byte = 1
            elif not (0 <= byte < 128):
                return False
        return mid_byte == 0