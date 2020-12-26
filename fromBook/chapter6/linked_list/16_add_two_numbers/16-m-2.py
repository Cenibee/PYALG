from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        upper = 0
        result = l1

        while l1:
            node_num = l1.val + upper
            if l2:
                node_num += l2.val
                l2 = l2.next

            upper, l1.val= divmod(node_num, 10)

            if not l1.next and not l2:
                if upper > 0:
                    l1.next = ListNode(1)
                break
            elif not l1.next and l2:
                l1.next, l1, l2 = l2, l2, l1.next
            else:
                l1 = l1.next
        return result


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
        list_to_list_node([5, 6, 3])))
print_node(
    sol.addTwoNumbers(
        list_to_list_node([9, 9, 9, 9]),
        list_to_list_node([9, 9, 9, 9, 9, 9, 9])))