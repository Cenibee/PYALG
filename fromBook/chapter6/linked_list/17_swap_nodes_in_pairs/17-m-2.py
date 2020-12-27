from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        before_result = head = ListNode(0, head)
        while head and head.next and head.next.next:
            first = head.next
            second = first.next

            head.next, first.next, second.next = second, second.next, first
            head = first

        return before_result.next

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

print_node(sol.swapPairs(list_to_list_node([1, 2, 3])))
print_node(sol.swapPairs(list_to_list_node([1, 2, 3, 4])))
print_node(sol.swapPairs(list_to_list_node([1, 2, 3, 4, 5])))
print_node(sol.swapPairs(list_to_list_node([1])))