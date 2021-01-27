class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head

        result = head = ListNode(None, head)

        while result and result.next:
            next_node = result.next

            while next_node and next_node.val == val:
                next_node = next_node.next

            result.next, result = next_node, next_node

        return head.next
