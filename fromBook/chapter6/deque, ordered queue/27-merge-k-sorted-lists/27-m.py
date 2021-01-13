# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
import sys

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        lists의 길이는 k 이고, 내부의 연결 리스트들은 오름차순으로 정렬 되어있다.
        모든 연결리스트를 정렬된 하나의 연결리스트로 병합하고, 이를 반환하라
        '''

        lists = list(filter(lambda x: x is not None, lists))

        root_node = last_node = ListNode(None, None)
        while len(lists) > 0:
            index, node = min(enumerate(lists), key=lambda x: x[1].val)

            if node.next is not None:
                lists[index] = node.next
            else:
                lists.pop(index)

            last_node.next, last_node = node, node

        return root_node.next


a = ListNode(2, None)
b = ListNode(1, None)
lists = [a, b]

print(min(enumerate(lists), key=lambda x: x[1].val))