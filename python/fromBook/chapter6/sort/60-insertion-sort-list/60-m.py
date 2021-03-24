# Definition for singly-linked list.
import sys
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head

        ans = node = ListNode(~sys.maxsize)

        while head:
            while node.next and node.next.val < head.val: node = node.next
            head.next, head, node.next = node.next, head.next, head

            # 최적 보고 추가한 코드 - 다음 거 비교 전에 마지막꺼보다 크면 초기화 안한다.
            if head and head.val < node.val:
                node = ans
        return ans.next

sol = Solution()
sol.insertionSortList(ListNode(4, ListNode(3, ListNode(2))))