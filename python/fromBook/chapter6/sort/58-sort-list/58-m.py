# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        mid, end = head, head.next

        while end.next and end.next.next:
            mid, end = mid.next, end.next.next

        mid.next, mid = None, mid.next
        head = self.sortList(head)
        mid = self.sortList(mid)

        temp = root = ListNode(None)
        while head and mid:
            if head.val <= mid.val:
                temp.next, head = head, head.next
            else:
                temp.next, mid = mid, mid.next
            temp = temp.next
        if head: temp.next = head
        if mid: temp.next = mid

        return root.next

sol = Solution()
sol.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))