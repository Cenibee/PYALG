from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_start = odd = ListNode(None)
        even_start = even = ListNode(None)

        while True:
            if head is not None:
                odd.next = head
                odd = head
                head, odd.next = head.next, None
            else: break

            if head is not None:
                even.next = head
                even = head
                head, even.next = head.next, None
            else: break

        odd.next = even_start.next

        return odd_start.next


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
print_node(sol.oddEvenList(list_to_list_node([1, 2, 3, 4, 5])))