from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(head: ListNode) -> ListNode:
            node, prev = head, None

            while node:
                next, node.next = node.next, prev
                prev, node = node, next

            return prev
        def toList(node: ListNode) -> ListNode:
            list:List = []
            while node:
                list.append(node.val)
                node = node.next
            return list

        def toReversedLinkedList(result:List):
            prev: ListNode = None
            for r in result:
                node = ListNode(r)
                node.next = prevprev = node
            return prev

        a = toList(reverseList(l1))
        b = toList(reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
            int(''.join(str(e) for e in b))

        return toReversedLinkedList(str(resultStr))