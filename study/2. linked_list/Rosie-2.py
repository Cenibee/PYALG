class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next

        return p1

sol = Solution()
print(sol.getIntersectionNode(ListNode(4, ListNode(1,ListNode(8,ListNode(4,ListNode(5))))),\
    ListNode(5,ListNode(6,ListNode(1,ListNode(8,ListNode(4,ListNode(5))))))))
