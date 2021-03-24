from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2

        result_head:ListNode = min(l1, l2, key=lambda x: x.val)
        last:ListNode = None

        while l1 and l2:
            if l1.val <= l2.val:
                if last:
                    last.next, last, l1 = l1, l1, l1.next
                else:
                    last, l1 = l1, l1.next
            else:
                if last:
                    last.next, last, l2 = l2, l2, l2.next
                else:
                    last, l2 = l2, l2.next

        if l1:
            last.next = l1
        elif l2:
            last.next = l2

        return result_head


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
print_node(sol.mergeTwoLists(list_to_list_node([1, 2, 4]), list_to_list_node([1, 3, 4])))