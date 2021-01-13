from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def sum(l1: ListNode, l2: ListNode, upper: bool) -> ListNode:
            if not l1 and not l2:
                if upper:
                    return ListNode(1)
                else:
                    return None
            if not l1:
                l1, l2 = l2, l1

            node_sum = l1.val

            if l2:
                node_sum += l2.val
                l2 = l2.next

            if upper:
                node_sum += 1

            l1.val = node_sum % 10
            l1.next = sum(l1.next, l2, node_sum > 9)
            return l1

        return sum(l1, l2, False)


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
print_node(
    sol.addTwoNumbers(
        list_to_list_node([2, 4, 3]),
        list_to_list_node([5, 6, 9])))
print_node(
    sol.addTwoNumbers(
        list_to_list_node([9, 9, 9, 9]),
        list_to_list_node([9, 9, 9, 9, 9, 9, 9])))