'''
leetcode 86. Partition List
https://leetcode.com/problems/partition-list/

연결 리스트의 헤드 head 와 값 x 가 주어졌을 때, x 보다 작은 값의 노드들이 x보다 크거나 같은 값의 노드들 보다 앞에 있도록 파티션을 분할하라
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 앞쪽에 붙일 리스트와 테일
        front = front_tail = ListNode(None)
        # 뒤쪽에 붙일 리스트와 테일
        back = back_tail = ListNode(None)

        # 전체 연길리스트를 순회
        while head:
            # val이 x 보다 작으면 앞쪽 테일에 연결
            if head.val < x:
                front_tail.next = head
                front_tail = front_tail.next
            # val이 x 보다 크거나 같으면 뒤쪽 테일에 연결
            else:
                back_tail.next = head
                back_tail = back_tail.next
            head = head.next

        # 앞쪽 테일에 뒤쪽 리스트를 잇고, 뒤쪽 테일다음을 None
        front_tail.next = back.next
        back_tail.next = None
        return front.next

sol = Solution()
# print(sol.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))),3))
print(sol.partition(ListNode(2, ListNode(1)),2))