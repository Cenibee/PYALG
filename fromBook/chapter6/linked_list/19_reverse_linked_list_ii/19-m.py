from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = before = ListNode(None, head)

        for _ in range(1, m):
            before, head = before.next, head.next

        reverse_start = head
        prev_node = next_node = None

        for _ in range(n - m + 1):
            next_node = head.next
            head.next  = prev_node
            prev_node, head = head, next_node

        before.next = prev_node
        reverse_start.next = next_node

        return root.next


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
    print()

sol = Solution()
print_node(sol.reverseBetween(list_to_list_node([1, 2, 3, 4, 5]), 2, 4))