from typing import List


class ListNode:
    def __init__(self, val=0, next=None, list=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        before_node = None

        while head.next:
            head.next, head, before_node = before_node, head.next, head

        head.next = before_node
        return head




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
print_node(sol.reverseList(list_to_list_node([1,2,3,4,5])))