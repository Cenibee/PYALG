'''
leetcode 876. Middle of the linked list
https://leetcode.com/problems/middle-of-the-linked-list/

비어있지 않은 단방향 연결리스트의 헤드 head가 주어졌을 때 중앙에 위치한 노드를 반환하라.
만약 중앙의 노드가 두개라면, 두 번째 중앙 노드를 반환한다.
'''
# 미리 정의된 연결 리스트 노드
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        투 포인터 중 런너 기법을 이용한다.
        '''
        # 두 칸씩 이동하는 fast, 한 칸씩 이동하는 slow 를 선언
        fast = slow = head

        # fast 가 이동이 불가할 때 까지 이동
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
