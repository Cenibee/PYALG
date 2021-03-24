from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        1. 사이즈 가져오고
        2. 중앙까지 포인터 반전하고
        3. 중앙에서부터 비교
        '''
        # 길이가 0, 1일 때
        if (not head or head.next == None):
            return True

        mid_count_flag = False
        before_mid:ListNode = head
        mid:ListNode = head.next
        now:ListNode = mid.next

        # 길이가 2일 때
        if not now:
            return head.val == mid.val

        while now.next is not None:
            now = now.next
            if mid_count_flag:
                # TODO 교환문 가독성 최적화
                # temp = mid.next
                # mid.next = before_mid
                # before_mid = mid
                # mid = temp
                temp, mid.next = mid.next, before_mid
                before_mid, mid = mid, temp
            mid_count_flag = not mid_count_flag

        right:ListNode = mid.next
        left:ListNode = mid if mid_count_flag else before_mid
        mid.next = before_mid

        while right is not None and left is not None:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True

def list_to_list_node(list: List) -> ListNode:
    node = None
    for i in range(-1, ~len(list), -1):
        node = ListNode(list[i], node)
    return node

def print_node(node: ListNode):
    while node.next is not None:
        print(node.val)
        node = node.next
    print(node.val)

sol = Solution()
print(sol.isPalindrome(list_to_list_node([1, 2, 3, 2, 3, 1])))
print(sol.isPalindrome(list_to_list_node([1, 2, 3, 1])))
print(sol.isPalindrome(list_to_list_node([1, 2])))
print(sol.isPalindrome(list_to_list_node([1, 0, 0])))
print()
print(sol.isPalindrome(list_to_list_node([1, 2, 3, 2, 1])))
print(sol.isPalindrome(list_to_list_node([1, 2, 2, 1])))
print(sol.isPalindrome(list_to_list_node([1, 2, 3, 3, 2, 1])))
print(sol.isPalindrome(list_to_list_node([1, 2, 1])))
print(sol.isPalindrome(list_to_list_node([1, 1])))